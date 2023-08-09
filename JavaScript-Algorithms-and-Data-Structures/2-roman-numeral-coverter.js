function convertToRoman(num) {
    let romanNum = ""
    while (num > 0) {
      if (num >= 1000) {
        num -= 1000;
        romanNum += 'M';
        continue}
      if (num >= 900) {
        num -= 900;
        romanNum += 'CM';
        continue}
      if (num >= 500) {
        num -= 500;
        romanNum += 'D';
        continue}
      if (num >= 400) {
        num -= 400;
        romanNum += 'CD';
        continue}
      if (num >= 100) {
        num -= 100;
        romanNum += 'C';
        continue}
      if (num >= 90) {
        num -= 90;
        romanNum += 'XC';
        continue}
      if (num >= 50) {
        num -= 50;
        romanNum += 'L';
        continue}
      if (num >= 40) {
        num -= 40;
        romanNum += 'XL';
        continue}
      if (num >= 10) {
        num -= 10;
        romanNum += 'X';
        continue}
      if (num >= 9) {
        num -= 9;
        romanNum += 'IX';
        continue}
      if (num >= 5) {
        num -= 5;
        romanNum += 'V';
        continue}
      if (num >= 4) {
        num -= 4;
        romanNum += 'IV';
        continue}
      if (num >= 1) {
        num -= 1;
        romanNum += 'I';
        continue}
    }
    console.log(romanNum)
    return romanNum;
  }
  
  console.log(convertToRoman(2555));