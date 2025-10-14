import json
import os

def create_locations():
    """
    Generates a JSON file containing a 100x100 grid of locations.
    """
    locations = {}
    grid_size = 100
    num_locations = grid_size * grid_size

    for n in range(1, num_locations + 1):
        location_name = f"l{n}"
        row = (n - 1) // grid_size
        col = (n - 1) % grid_size

        location = {
            "in-zone": "z1",
            "type": "outside",
            "entities": [],
            "exits": {}
        }

        # Directions: N, NE, E, SE, S, SW, W, NW
        # Exit codes: 0, 45, 90, 135, 180, 225, 270, 315
        # Deltas: (d_row, d_col)
        directions = {
            "0": (-1, 0),   # N
            "45": (-1, 1),  # NE
            "90": (0, 1),   # E
            "135": (1, 1),  # SE
            "180": (1, 0),  # S
            "225": (1, -1), # SW
            "270": (0, -1), # W
            "315": (-1, -1) # NW
        }

        for exit_code, (d_row, d_col) in directions.items():
            n_row, n_col = row + d_row, col + d_col

            if 0 <= n_row < grid_size and 0 <= n_col < grid_size:
                neighbor_n = n_row * grid_size + n_col + 1
                neighbor_name = f"l{neighbor_n}"
                location["exits"][exit_code] = {"to": neighbor_name}

        locations[location_name] = location

    output_dir = "gdata"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, "locations.json"), "w") as f:
        json.dump(locations, f, indent=4)

if __name__ == "__main__":
    create_locations()
    print("gdata/locations.json created successfully.")
