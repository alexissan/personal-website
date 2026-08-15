const PROTECTED_PREFIXES = ['/lab', '/cleaning-windows', '/api'];
const SESSION_COOKIE = 'as_session';
const SESSION_TTL_SECONDS = 60 * 60 * 24 * 30;
const ALLOWED_ORIGIN = 'https://alexissantos.dev';
const BOOKINGS_KEY = 'custom_bookings';

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
  'Access-Control-Allow-Credentials': 'true',
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          ...CORS_HEADERS,
          'Access-Control-Allow-Methods': 'GET, POST, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type',
          'Vary': 'Origin',
        },
      });
    }

    if (isProtected(url.pathname)) {
      const session = await authorize(request, env);

      if (!session.ok) {
        return unauthorized();
      }

      const response = await route(request, url, env);

      if (session.setCookie) {
        const headers = new Headers(response.headers);
        headers.append('Set-Cookie', session.setCookie);
        return new Response(response.body, {
          status: response.status,
          statusText: response.statusText,
          headers,
        });
      }

      return response;
    }

    return route(request, url, env);
  },
};

function isProtected(pathname) {
  return PROTECTED_PREFIXES.some(
    prefix => pathname === prefix || pathname.startsWith(`${prefix}/`)
  );
}

async function authorize(request, env) {
  const secret = env.LAB_PASSWORD;

  if (!secret) {
    return { ok: false };
  }

  const cookie = readCookie(request, SESSION_COOKIE);

  if (cookie && (await isValidSession(cookie, secret))) {
    return { ok: true };
  }

  const header = request.headers.get('Authorization') || '';

  if (header.startsWith('Basic ')) {
    let decoded;

    try {
      decoded = atob(header.slice(6));
    } catch {
      return { ok: false };
    }

    const password = decoded.slice(decoded.indexOf(':') + 1);

    if (constantTimeEquals(password, secret)) {
      return { ok: true, setCookie: await mintSession(secret) };
    }
  }

  return { ok: false };
}

function unauthorized() {
  return new Response('Authentication required.\n', {
    status: 401,
    headers: {
      'WWW-Authenticate': 'Basic realm="alexissantos.dev", charset="UTF-8"',
      'Cache-Control': 'no-store',
      'Content-Type': 'text/plain; charset=utf-8',
      'X-Robots-Tag': 'noindex, nofollow',
    },
  });
}

async function mintSession(secret) {
  const expires = Math.floor(Date.now() / 1000) + SESSION_TTL_SECONDS;
  const signature = await sign(String(expires), secret);
  return `${SESSION_COOKIE}=${expires}.${signature}; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=${SESSION_TTL_SECONDS}`;
}

async function isValidSession(value, secret) {
  const separator = value.lastIndexOf('.');

  if (separator === -1) {
    return false;
  }

  const expires = value.slice(0, separator);
  const signature = value.slice(separator + 1);

  if (!/^\d+$/.test(expires) || Number(expires) < Math.floor(Date.now() / 1000)) {
    return false;
  }

  return constantTimeEquals(signature, await sign(expires, secret));
}

async function sign(message, secret) {
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw',
    encoder.encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  );
  const signature = await crypto.subtle.sign('HMAC', key, encoder.encode(message));

  let binary = '';
  for (const byte of new Uint8Array(signature)) {
    binary += String.fromCharCode(byte);
  }

  return btoa(binary).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function constantTimeEquals(a, b) {
  if (a.length !== b.length) {
    return false;
  }

  let difference = 0;
  for (let i = 0; i < a.length; i++) {
    difference |= a.charCodeAt(i) ^ b.charCodeAt(i);
  }

  return difference === 0;
}

function readCookie(request, name) {
  const header = request.headers.get('Cookie');

  if (!header) {
    return null;
  }

  for (const part of header.split(';')) {
    const [key, ...rest] = part.trim().split('=');
    if (key === name) {
      return rest.join('=');
    }
  }

  return null;
}

function route(request, url, env) {
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
}

async function handleBookings(request, env) {
  if (request.method === 'GET') {
    const data = await env.BOOKINGS_KV.get(BOOKINGS_KEY);
    const bookings = data ? JSON.parse(data) : [];
    return new Response(JSON.stringify(bookings), {
      headers: {
        'Content-Type': 'application/json',
        ...CORS_HEADERS,
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
        ...CORS_HEADERS,
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
      ...CORS_HEADERS,
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
        ...CORS_HEADERS,
      },
    });
  }

  let target;

  try {
    target = new URL(icalUrl);
  } catch {
    return new Response(JSON.stringify({ error: 'Invalid url parameter' }), {
      status: 400,
      headers: {
        'Content-Type': 'application/json',
        ...CORS_HEADERS,
      },
    });
  }

  if (target.protocol !== 'https:' && target.protocol !== 'webcal:') {
    return new Response(JSON.stringify({ error: 'Unsupported protocol' }), {
      status: 400,
      headers: {
        'Content-Type': 'application/json',
        ...CORS_HEADERS,
      },
    });
  }

  if (target.protocol === 'webcal:') {
    target.protocol = 'https:';
  }

  try {
    const response = await fetch(target.toString(), {
      headers: {
        'User-Agent': 'CleaningWindows/1.0',
      },
    });

    if (!response.ok) {
      return new Response(JSON.stringify({ error: `Failed to fetch: ${response.status}` }), {
        status: response.status,
        headers: {
          'Content-Type': 'application/json',
          ...CORS_HEADERS,
        },
      });
    }

    const icalData = await response.text();

    return new Response(icalData, {
      headers: {
        'Content-Type': 'text/calendar',
        ...CORS_HEADERS,
        'Cache-Control': 'private, max-age=300',
      },
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json',
        ...CORS_HEADERS,
      },
    });
  }
}
