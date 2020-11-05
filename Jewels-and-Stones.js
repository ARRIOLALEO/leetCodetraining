var numJewelsInStones = function(J, S) {
    const ju = J.split("")
    const stoner = S.split("")
    let conunter = 0;
      ju.map(ju => conunter = conunter + stoner.filter(stn=> stn === ju).length)
    return conunter
};
console.log(numJewelsInStones("aA","aAAbbbb"))
