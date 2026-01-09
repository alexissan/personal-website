const CONFIG = {
  workerUrl: '/api/ical-proxy',

  properties: [
    {
      id: 'estudio-jessica',
      name: 'El estudio de Jessica',
      color: '#8b5cf6',
      calendars: [
        { name: 'Airbnb', url: 'https://www.airbnb.com/calendar/ical/909530985231915672.ics?t=64ef41c74cdf490e98d6d032b676b2fc' },
        { name: 'Booking.com', url: 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=767a381b-feb5-4f79-a4dd-f1008704f271' },
      ],
    },
    {
      id: 'apartamento-margot',
      name: 'El apartamento de Margot',
      color: '#ec4899',
      calendars: [
        { name: 'Airbnb', url: 'https://www.airbnb.com/calendar/ical/1018266727128965155.ics?t=a93dfa033801443bad1b042782467616' },
        { name: 'Booking.com', url: 'https://ical.booking.com/v1/export?t=d725c7d6-ad28-4d2f-a882-b615b8eac657' },
      ],
    },
  ],
};
