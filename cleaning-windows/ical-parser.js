function parseIcalDate(dateStr) {
  if (!dateStr) return null;

  dateStr = dateStr.replace(/^(DTSTART|DTEND)[^:]*:/, '');

  if (dateStr.length === 8) {
    const year = parseInt(dateStr.substring(0, 4));
    const month = parseInt(dateStr.substring(4, 6)) - 1;
    const day = parseInt(dateStr.substring(6, 8));
    return new Date(year, month, day);
  }

  if (dateStr.includes('T')) {
    const year = parseInt(dateStr.substring(0, 4));
    const month = parseInt(dateStr.substring(4, 6)) - 1;
    const day = parseInt(dateStr.substring(6, 8));
    const hour = parseInt(dateStr.substring(9, 11));
    const minute = parseInt(dateStr.substring(11, 13));
    const second = parseInt(dateStr.substring(13, 15));

    if (dateStr.endsWith('Z')) {
      return new Date(Date.UTC(year, month, day, hour, minute, second));
    }
    return new Date(year, month, day, hour, minute, second);
  }

  return null;
}

function parseIcal(icalData) {
  const events = [];
  const lines = icalData.split(/\r?\n/);

  let currentEvent = null;
  let currentKey = null;
  let currentValue = '';

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    if (line.startsWith(' ') || line.startsWith('\t')) {
      currentValue += line.substring(1);
      continue;
    }

    if (currentKey && currentEvent) {
      processLine(currentEvent, currentKey, currentValue);
    }

    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) {
      currentKey = null;
      currentValue = '';
      continue;
    }

    currentKey = line.substring(0, colonIndex);
    currentValue = line.substring(colonIndex + 1);

    if (line === 'BEGIN:VEVENT') {
      currentEvent = {};
      currentKey = null;
    } else if (line === 'END:VEVENT' && currentEvent) {
      if (currentEvent.start && currentEvent.end) {
        events.push(currentEvent);
      }
      currentEvent = null;
      currentKey = null;
    }
  }

  return events;
}

function processLine(event, key, value) {
  if (key.startsWith('DTSTART')) {
    event.start = parseIcalDate(value);
  } else if (key.startsWith('DTEND')) {
    event.end = parseIcalDate(value);
  } else if (key === 'SUMMARY') {
    event.summary = value;
  } else if (key === 'UID') {
    event.uid = value;
  }
}

async function fetchIcal(workerUrl, icalUrl) {
  const proxyUrl = `${workerUrl}?url=${encodeURIComponent(icalUrl)}`;
  const response = await fetch(proxyUrl);

  if (!response.ok) {
    throw new Error(`Failed to fetch iCal: ${response.status}`);
  }

  return await response.text();
}

async function loadCalendarsForProperty(workerUrl, property) {
  const allEvents = [];

  for (const calendar of property.calendars) {
    try {
      const icalData = await fetchIcal(workerUrl, calendar.url);
      const events = parseIcal(icalData);
      events.forEach(event => {
        event.source = calendar.name;
        event.propertyId = property.id;
        event.propertyName = property.name;
        event.propertyColor = property.color;
      });
      allEvents.push(...events);
    } catch (error) {
      console.error(`Failed to load ${calendar.name} calendar for ${property.name}:`, error);
    }
  }

  return allEvents;
}
