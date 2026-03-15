export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type',
        },
      });
    }

    // Proxy /dashboard to Vercel (OpenClaw)
    // Vercel app runs at root — strip /dashboard prefix before forwarding
    if (url.pathname === '/dashboard' || url.pathname.startsWith('/dashboard/')) {
      const strippedPath = url.pathname.replace(/^\/dashboard/, '') || '/';
      const vercelUrl = new URL(strippedPath + url.search, 'https://openclaw-dashboard-mauve.vercel.app');

      const headers = new Headers(request.headers);
      headers.set('x-forwarded-host', url.hostname);
      headers.set('x-forwarded-proto', 'https');
      headers.set('x-base-path', '/dashboard');

      const res = await fetch(vercelUrl.toString(), {
        method: request.method,
        headers,
        body: request.method !== 'GET' && request.method !== 'HEAD' ? request.body : undefined,
        redirect: 'manual',
      });

      // Rewrite redirects to include /dashboard prefix
      const status = res.status;
      if (status >= 300 && status < 400) {
        const location = res.headers.get('location');
        if (location) {
          try {
            const redirectUrl = new URL(location, vercelUrl);
            // Only rewrite if redirecting within the Vercel app
            if (redirectUrl.hostname === 'openclaw-dashboard-mauve.vercel.app') {
              redirectUrl.hostname = url.hostname;
              redirectUrl.protocol = url.protocol;
              redirectUrl.pathname = '/dashboard' + redirectUrl.pathname;
            }
            return Response.redirect(redirectUrl.toString(), status);
          } catch {
            // If URL parsing fails, pass through as-is
          }
        }
      }

      // Rewrite HTML responses to fix asset paths and links
      const contentType = res.headers.get('content-type') || '';
      if (contentType.includes('text/html')) {
        let html = await res.text();
        // Fix Next.js asset paths: /_next/ -> /dashboard/_next/
        html = html.replaceAll('"/_next/', '"/dashboard/_next/');
        html = html.replaceAll("'/_next/", "'/dashboard/_next/");
        // Fix links: href="/" -> href="/dashboard/"
        html = html.replaceAll('href="/', 'href="/dashboard/');
        // Fix fetch/API paths in inline scripts
        html = html.replaceAll('"/_next/', '"/dashboard/_next/');

        const newHeaders = new Headers(res.headers);
        newHeaders.delete('content-encoding');
        return new Response(html, {
          status: res.status,
          statusText: res.statusText,
          headers: newHeaders,
        });
      }

      return res;
    }

    // Proxy /dashboard/_next/ static assets (already handled above, but just in case)
    if (url.pathname.startsWith('/dashboard/_next/')) {
      const assetPath = url.pathname.replace(/^\/dashboard/, '');
      const vercelUrl = new URL(assetPath + url.search, 'https://openclaw-dashboard-mauve.vercel.app');
      return fetch(vercelUrl.toString(), { headers: request.headers });
    }

    if (url.pathname === '/api/ical-proxy') {
      return handleIcalProxy(request);
    }

    if (url.pathname === '/api/bookings') {
      return handleBookings(request, env);
    }

    if (url.pathname.startsWith('/api/bookings/')) {
      return handleBookingDelete(request, url, env);
    }

    return env.ASSETS.fetch(request);
  },
};

const BOOKINGS_KEY = 'custom_bookings';

async function handleBookings(request, env) {
  if (request.method === 'GET') {
    const data = await env.BOOKINGS_KV.get(BOOKINGS_KEY);
    const bookings = data ? JSON.parse(data) : [];
    return new Response(JSON.stringify(bookings), {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });
  }

  if (request.method === 'POST') {
    const body = await request.json();
    const data = await env.BOOKINGS_KV.get(BOOKINGS_KEY);
    const bookings = data ? JSON.parse(data) : [];

    const newBooking = {
      id: Date.now().toString(),
      propertyId: body.propertyId,
      start: body.start,
      end: body.end,
      note: body.note || '',
    };

    bookings.push(newBooking);
    await env.BOOKINGS_KV.put(BOOKINGS_KEY, JSON.stringify(bookings));

    return new Response(JSON.stringify(newBooking), {
      status: 201,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });
  }

  return new Response('Method not allowed', { status: 405 });
}

async function handleBookingDelete(request, url, env) {
  if (request.method !== 'DELETE') {
    return new Response('Method not allowed', { status: 405 });
  }

  const id = url.pathname.split('/').pop();
  const data = await env.BOOKINGS_KV.get(BOOKINGS_KEY);
  let bookings = data ? JSON.parse(data) : [];

  bookings = bookings.filter(b => b.id !== id);
  await env.BOOKINGS_KV.put(BOOKINGS_KEY, JSON.stringify(bookings));

  return new Response(JSON.stringify({ success: true }), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    },
  });
}

async function handleIcalProxy(request) {
  const url = new URL(request.url);
  const icalUrl = url.searchParams.get('url');

  if (!icalUrl) {
    return new Response(JSON.stringify({ error: 'Missing url parameter' }), {
      status: 400,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });
  }

  try {
    const response = await fetch(icalUrl, {
      headers: {
        'User-Agent': 'CleaningWindows/1.0',
      },
    });

    if (!response.ok) {
      return new Response(JSON.stringify({ error: `Failed to fetch: ${response.status}` }), {
        status: response.status,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
      });
    }

    const icalData = await response.text();

    return new Response(icalData, {
      headers: {
        'Content-Type': 'text/calendar',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=300',
      },
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });
  }
}
