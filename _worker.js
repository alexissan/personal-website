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
