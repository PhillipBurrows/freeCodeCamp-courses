function telephoneCheck(str) {
  console.log(str)
  //count more than 11 f
  var count = (str.match(/\d/g) || []).length
  if (count > 11) {return false}
  if (count == 11) {
    if (/^[^1]/.test(str)) {
      return false
    }
  }
  //random characters f
  if (/[^0-9-\s()]/g.test(str)) {
    return false
  }

  if (/^[\d]{10}$/.test(str)) {
    return true
  }
  if (/^[0-9]{3}-[0-9]{3}-[0-9]{4}$/.test(str)) {
    return true
  }
  if (/^\([\d]{3}\)[\d]{3}-[\d]{4}$/.test(str)) {
    return true
  }
  if (/^\([\d]{3}\) [\d]{3}-[\d]{4}$/.test(str)) {
    return true
  }
  if (/^[\d]{3} [\d]{3} [\d]{4}$/.test(str)) {
    return true
  }
  if (/^1 [0-9]{3} [0-9]{3} [0-9]{4}$/.test(str)) {
    return true
  }
  if (/^[\d]{10}$/.test(str)) {
    return true
  }
  if (/^1 [\d]{3}-[\d]{3}-[\d]{4}$/.test(str)) {
    return true
  }
  if (/^1 \([\d]{3}\) [\d]{3}-[\d]{4}$/.test(str)) {
    return true
  }
  if (/^1\([\d]{3}\)[\d]{3}-[\d]{4}$/.test(str)) {
    return true
  }
  else {
    return false
  }
}  
 
telephoneCheck("5555555555");