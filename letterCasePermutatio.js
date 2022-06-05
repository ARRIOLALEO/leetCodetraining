var letterCasePermutation = function(s) {
    const unique = new Set()
    s.toLowerCase()
    s = [...s]
    const sizeS = s.length
    function backtracking(temp,position){
        if((temp.length) === sizeS){
            unique.add([...temp].join(""))
            return
        }
        backtracking([...temp,s[position].toLowerCase()],position+1)
        backtracking([...temp,s[position].toUpperCase()],position+1)
    }
    backtracking([],0)
    return [...unique]
};
