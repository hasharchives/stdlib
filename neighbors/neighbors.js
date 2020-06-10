function on_position(a, neighbors) {
  /** Returns all neighbors that share an agent's position */
  if (!a.position) {
    throw new Error("agent must have position");
  }
  on_pos = [];
  neighbors.forEach((neighbor) => {
    if (
      a.position[0] === neighbor.position[0] &&
      a.position[1] === neighbor.position[1] &&
      a.position[2] === neighbor.position[2]
    ) {
      on_pos.push(neighbor);
    }
  })

  return on_pos;
}

function in_radius(a, neighbors, radius = 1) {
  /** Returns all neighbors within a certain vision radius of an agent.
  *   Defaults vision radius to 1
  */
  if (!a.position) {
    throw new Error("agent must have position");
  }
  x_bounds = [a.position[0] + radius, a.position[0] - radius];
  y_bounds = [a.position[1] + radius, a.position[1] - radius];
  z_bounds = [a.position[2] + radius, a.position[2] - radius];

  in_rad = []
  neighbors.forEach((neighbor) => {
    if (
      neighbor.position[0] <= x_bounds[0] &&
      neighbor.position[0] >= x_bounds[1] &&
      neighbor.position[1] <= y_bounds[0] &&
      neighbor.position[1] >= y_bounds[1] &&
      neighbor.position[2] <= z_bounds[0] &&
      neighbor.position[2] >= z_bounds[1]
    ) {
      in_rad.push(neighbor);
    }
  })

  return in_rad;
}

function in_front(a, neighbors) {
  /** Searches and returns all neighbors whose position is in front of an agent*/
  if (!a.position) {
    throw new Error("agent must have position");
  }

  n_front = []
  neighbors.forEach((neighbor) => {
    if (
      neighbor.position[0] >= a.position[0] &&
      neighbor.position[1] >= a.position[1] &&
      neighbor.position[0] !== a.position[0] &&
      neighbor.position[1] !== a.position[1]
    ) {
      n_front.push(neighbor);
    }
  })

  return n_front;
}

module.exports = { on_position, in_radius, in_front }