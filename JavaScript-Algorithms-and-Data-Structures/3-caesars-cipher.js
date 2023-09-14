const alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];

function isNotCapAlpha(str) {
  return !str.match(/[A-Z]/i)
}

function rot13(str) {
  let decipheredStr = ''
  for (let i = 0; i < str.length; i++) {
    var position = alphabet.indexOf(str[i]) + 13;
    
    if (isNotCapAlpha(str[i])) {
      decipheredStr += str[i]
    } else if (position < 26) {
      decipheredStr += alphabet[position];
    } else {
      position -= 26
      decipheredStr += alphabet[position]
    }
  }
  
  console.log(decipheredStr)
  return decipheredStr;
}

rot13("SERR PBQR PNZC");