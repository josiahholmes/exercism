export const COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"];

export const value = (colors) => {
  // only return the first two values in array
  colors.splice(2);
  // return array with index values for colors in COLORS
  const values = colors.map((color) => COLORS.indexOf(color));
  // join index values and convert to number
  return Number(values.join(''));
};