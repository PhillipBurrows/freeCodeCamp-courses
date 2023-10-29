function checkCashRegister(price, cash, cid) {
    let total_cid = 0;
    for (var i = 0; i < cid.length; i++) {
      total_cid += cid[i][1]
    }
    let total_due = cash - price;
  
    if (total_cid < total_due) {
      return {status: 'INSUFFICIENT_FUNDS', change: []}
    }
    
    let change_due = [["PENNY", 0], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]
  
    //let change;
    //return change;
  }
  
  //checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);