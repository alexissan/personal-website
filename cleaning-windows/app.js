let allEvents = [];
let cleaningWindows = [];
let currentView = 'list';
let currentMonth = new Date();

function calculateCleaningWindows(events) {
  const windowsByProperty = {};

  for (const property of CONFIG.properties) {
    const propertyEvents = events
      .filter(e => e.propertyId === property.id)
      .sort((a, b) => a.start - b.start);

    const windows = [];

    for (let i = 0; i < propertyEvents.length - 1; i++) {
      const currentCheckout = propertyEvents[i].end;
      const nextCheckin = propertyEvents[i + 1].start;

      if (currentCheckout < nextCheckin) {
        const days = Math.ceil((nextCheckin - currentCheckout) / (1000 * 60 * 60 * 24));
        windows.push({
          propertyId: property.id,
          propertyName: property.name,
          propertyColor: property.color,
          start: currentCheckout,
          end: nextCheckin,
          days: days,
          isUrgent: days === 1,
          urgencyLevel: days === 1 ? 'urgent' : days === 2 ? 'warning' : 'normal',
        });
      }
    }

    windowsByProperty[property.id] = windows;
  }

  return windowsByProperty;
}

function formatDate(date) {
  return date.toLocaleDateString('en-GB', {
    weekday: 'short',
    day: 'numeric',
    month: 'short',
  });
}

function renderListView(windowsByProperty) {
  const container = document.getElementById('content');
  let html = '';

  const today = new Date();
  today.setHours(0, 0, 0, 0);

  for (const property of CONFIG.properties) {
    const windows = windowsByProperty[property.id] || [];
    const futureWindows = windows.filter(w => w.end >= today);

    html += `<div class="property-section">`;
    html += `<h2 class="property-name" style="border-left-color: ${property.color}">${property.name}</h2>`;

    if (futureWindows.length === 0) {
      html += `<p class="no-windows">No upcoming cleaning windows</p>`;
    } else {
      html += `<div class="windows-list">`;
      for (const window of futureWindows) {
        const urgencyClass = window.urgencyLevel;
        html += `
          <div class="window-item ${urgencyClass}">
            <span class="urgency-badge ${urgencyClass}">
              ${window.isUrgent ? 'URGENT' : window.days + ' days'}
            </span>
            <span class="window-dates">
              ${formatDate(window.start)} &rarr; ${formatDate(window.end)}
            </span>
          </div>
        `;
      }
      html += `</div>`;
    }

    html += `</div>`;
  }

  container.innerHTML = html;
}

function renderCalendarView(windowsByProperty) {
  const container = document.getElementById('content');

  const year = currentMonth.getFullYear();
  const month = currentMonth.getMonth();
  const monthName = currentMonth.toLocaleDateString('en-GB', { month: 'long', year: 'numeric' });

  let html = `
    <div class="calendar-header">
      <button class="nav-btn" onclick="prevMonth()">&larr;</button>
      <h2>${monthName}</h2>
      <button class="nav-btn" onclick="nextMonth()">&rarr;</button>
    </div>
  `;

  for (const property of CONFIG.properties) {
    html += renderPropertyCalendar(property, windowsByProperty[property.id] || [], year, month);
  }

  container.innerHTML = html;
}

function renderPropertyCalendar(property, windows, year, month) {
  const firstDay = new Date(year, month, 1);
  const lastDay = new Date(year, month + 1, 0);
  const startDay = firstDay.getDay();
  const daysInMonth = lastDay.getDate();

  const propertyEvents = allEvents.filter(e => e.propertyId === property.id);

  let html = `
    <div class="property-calendar">
      <h3 class="property-calendar-title" style="border-left-color: ${property.color}">${property.name}</h3>
      <div class="calendar-grid">
        <div class="calendar-day-header">S</div>
        <div class="calendar-day-header">M</div>
        <div class="calendar-day-header">T</div>
        <div class="calendar-day-header">W</div>
        <div class="calendar-day-header">T</div>
        <div class="calendar-day-header">F</div>
        <div class="calendar-day-header">S</div>
  `;

  for (let i = 0; i < startDay; i++) {
    html += `<div class="calendar-cell empty"></div>`;
  }

  for (let day = 1; day <= daysInMonth; day++) {
    const date = new Date(year, month, day);
    const isToday = isSameDay(date, new Date());

    let cellClass = 'calendar-cell';
    let status = '';

    for (const event of propertyEvents) {
      if (isDateInRange(date, event.start, event.end)) {
        cellClass += ' booked';
        status = 'booked';
        break;
      }
    }

    if (!status) {
      for (const window of windows) {
        if (isDateInRange(date, window.start, window.end)) {
          cellClass += ` cleaning ${window.urgencyLevel}`;
          status = 'cleaning';
          break;
        }
      }
    }

    const dayClass = isToday ? 'day-number today' : 'day-number';
    html += `<div class="${cellClass}"><span class="${dayClass}">${day}</span></div>`;
  }

  html += `
      </div>
      <div class="calendar-mini-legend">
        <span class="legend-booked">Booked</span>
        <span class="legend-cleaning">Cleaning</span>
      </div>
    </div>
  `;

  return html;
}

function isDateInRange(date, start, end) {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  const s = new Date(start);
  s.setHours(0, 0, 0, 0);
  const e = new Date(end);
  e.setHours(0, 0, 0, 0);
  return d >= s && d < e;
}

function isSameDay(d1, d2) {
  return d1.getFullYear() === d2.getFullYear() &&
         d1.getMonth() === d2.getMonth() &&
         d1.getDate() === d2.getDate();
}

function prevMonth() {
  currentMonth.setMonth(currentMonth.getMonth() - 1);
  renderCalendarView(cleaningWindows);
}

function nextMonth() {
  currentMonth.setMonth(currentMonth.getMonth() + 1);
  renderCalendarView(cleaningWindows);
}

function switchView(view) {
  currentView = view;
  document.querySelectorAll('.view-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelector(`[data-view="${view}"]`).classList.add('active');

  if (view === 'list') {
    renderListView(cleaningWindows);
  } else {
    renderCalendarView(cleaningWindows);
  }
}

async function loadAllData() {
  const container = document.getElementById('content');
  container.innerHTML = '<div class="loading">Loading calendars...</div>';

  allEvents = [];

  for (const property of CONFIG.properties) {
    try {
      const events = await loadCalendarsForProperty(CONFIG.workerUrl, property);
      allEvents.push(...events);
    } catch (error) {
      console.error(`Failed to load ${property.name}:`, error);
    }
  }

  cleaningWindows = calculateCleaningWindows(allEvents);

  if (currentView === 'list') {
    renderListView(cleaningWindows);
  } else {
    renderCalendarView(cleaningWindows);
  }
}

function refreshData() {
  const btn = document.querySelector('.refresh-btn');
  btn.classList.add('spinning');
  loadAllData().finally(() => {
    btn.classList.remove('spinning');
  });
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.view-btn').forEach(btn => {
    btn.addEventListener('click', () => switchView(btn.dataset.view));
  });

  loadAllData();
});
