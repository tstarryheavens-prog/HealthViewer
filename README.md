# HealthViewer

A browser-based health and wellness dashboard for tracking daily metrics, workouts, nutrition, sleep, and habits.

## Features

- Personalized health overview with key metrics at a glance
- Activity & workout tracking
- Nutrition and hydration logging
- Sleep quality monitoring
- Daily habit tracker with streaks
- Responsive design that works on any device

## Getting Started

### Prerequisites

- Python 3.8+ (the included `app.py` is compatible)

### Run Locally

```bash
python app.py
```

The server starts at `http://localhost:8080`. Open it in your browser to see the dashboard.

### API Endpoints

| Endpoint           | Method | Description               |
|--------------------|--------|---------------------------|
| `/`                | GET    | Serves the HTML page      |
| `/api/`            | GET    | Returns a JSON status     |

## License

MIT License
