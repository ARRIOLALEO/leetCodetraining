function findJudge(n: number, trust: number[][]): number {

    const inOutDegrees:number[] = Array(n + 1).fill(0);    // SC: O(n)
    trust.forEach(([trustee, trusted]) => {    // TC: O(n)
        --inOutDegrees[trustee];    // out-degree
        ++inOutDegrees[trusted];    // in-degree
    })
    for(let i = 1; i <= n; ++i) {    // TC: O(n)
        if(inOutDegrees[i] === n - 1) {
            return i;
        }
    }
    return -1;
};
