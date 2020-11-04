/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    const sorted = nums.sort()
    const s = new Set(nums).values();
    let response = []
    let solution = []
    let sume = 0
    for (let letter of s) {
        response.push(letter);
    }
    response.map(item => {
        const e = nums.filter(i => i === item)
        solution.push((e.length * (e.length - 1)) / 2)
    })

    solution.map(item => sume = sume + item)
    return sume
};
