# wsim - World Simulator

This project is a world simulator with a Python Flask backend.

## Setup

This project is designed to be run on Ubuntu 24.

### Prerequisites

- Python 3.10+
- `venv`

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/wsim.git
    cd wsim
    ```

2.  Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

### Development

To run the server in development mode, run the following command:

```bash
python -m wsim
```

The server will be running at `http://localhost:5000`.

### Production

To run the server in production, it is recommended to use a production-ready WSGI server like Gunicorn.

1.  Install Gunicorn:

    ```bash
    pip install gunicorn
    ```

2.  Run the server with Gunicorn:

    ```bash
    gunicorn "wsim.__main__:app"
    ```

## Testing

This project uses `tox` for testing. To run the tests, run the following command:

```bash
tox
```

This will create a virtual environment, install the dependencies, and run the tests.

### Running Tests Manually

To run the tests manually, run the following command:

```bash
pytest
```

### Testing with `curl`

Each API call can be tested with `curl`.

**Get all entities:**

```bash
curl http://localhost:5000/wsim/v1/entities
```

**Get all locations:**

```bash
curl http://localhost:5000/wsim/v1/locations
```

**Get all zones:**

```bash
curl http://localhost:5000/wsim/v1/zones
```

**Get all entity info:**

```bash
curl http://localhost:5000/wsim/v1/entityInfo
```