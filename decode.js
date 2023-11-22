
const encode = s=> {

const a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
const b=  "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    if(a.indexOf(s) >=0){
        return b[a.indexOf(s)]
    } 
    return s
}

const d = "if we're gonna live, we'll live together, but if we're gonna die, i'd rather die with you."
const d2 = `
A constellation is an area on the celestial sphere in which a group of visible stars forms a perceived pattern or outline
, typically representing an animal, mythological subject, or inanimate object.[1]

The origins of the earliest constellations likely go back to prehistory. 
People used them to relate stories of their beliefs, experiences, creation, or mythology. 
Different cultures and countries invented their own constellations, some of which lasted into the early 20th century before today's constellations were internationally recognized. 
The recognition of constellations has changed significantly over time. Many changed in size or shape. 
Some became popular, only to drop into obscurity. Some were limited to a single culture or nation. 
Naming constellations also helped astronomers and navigators identify stars more easily.[2]`



let temp = ""
for(var i=0;i<d2.length;i++){
    temp+=encode(d2[i])
}
console.log("______________________________________________")
console.log(temp)


const decode = s=> {

    const a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    const b=  "kx*mcnoph*rs*yi*adlegwruftKX*MCNOPH*RS*YI*ADLEGWRUFT"
    
        if(a.indexOf(s) >=0){
            return b[a.indexOf(s)]
        } 
        return s
    }

let temp2 =""

for(var i=0;i<d2.length;i++){
    temp2+=decode(temp[i])
}

console.log(temp2)
