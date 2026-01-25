// var str = "How can mirrors be real if our eyes aren't real";

// String.prototype.toJadenCase = function () {
//   return str
//     .split(" ")
//     .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
//     .join(" ");
// };

// console.log(str.toJadenCase());

function isIsogram(str) {
  const lc = str.toLowerCase();
  return new Set(lc).size === str.length;
}

console.log(isIsogram("yuhh"));
