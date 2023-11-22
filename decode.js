
const decode = s=> {

const a = "abcdefghijklmnopqrstuvwxyz"
const b=  "qwertyuiopasdfghjklzxcvbnm"

    if(a.indexOf(s) >=0){
        return b[a.indexOf(s)]
    } 
    return s
}

const d = "if we're gonna live, we'll live together, but if we're gonna die, i'd rather die with you."
let temp = ""
for(var i=0;i<d.length;i++){
    temp+=decode(d[i])
}

console.log(temp)