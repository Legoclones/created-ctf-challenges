# Web bad
**Level**: Extreme

**Points**: 650

**Author**: Justin Applegate

**Writeup by**: Justin Applegate

**Description**:
```markdown
How about an HTML version of bad??

[bad.html]
```

## Writeup
All we are given here is a single HTML page which verifies if an inputted flag is correct. Line 12 of the code reveals that a function called `á̃̂̄̅` is run each time the "Check flag" button is submitted. Below is the following script:

```javascript
var á̃̄̅̂=eval(atob("ZG9jdW1lbnQ="));var á̂̅̃̄=eval(atob("U3RyaW5n"));var á̃̄̂̅=á̃̄̅̂.getElementById.bind(á̃̄̅̂);var á̂̅̄̃=á̂̅̃̄.fromCharCode.bind(á̂̅̃̄);á̂̅̃̄.prototype.á̂̄̃̅=á̂̅̃̄.prototype.substr;var á̃̂̅̄=(ấ̄̅̃,ấ̄̃̅)=>{var ấ̃̅̄=[];var ấ̃̄̅="";for(á̃̅̂̄=eval(atob("U3RyaW5nLmxlbmd0aA=="));á̃̅̂̄<='bGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKcpOwbGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKcpOwbGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKc'.length;á̃̅̂̄++){ấ̃̅̄[á̂̅̄̃(á̃̅̂̄)]=á̃̅̂̄}for(á̂̄̅̃=á̃̅̂̄=eval(atob("U3RyaW5nLnByb3RvdHlwZS5nZXRyZWt0PVN0cmluZy5wcm90b3R5cGUubGVuZ3RoO1N0cmluZy5wcm90b3R5cGUuZ2V0cmVrdA=="));á̃̅̂̄<ấ̄̅̃.length;á̃̅̂̄++){ấ̃̄̅+=á̂̅̄̃(ấ̃̅̄[ấ̄̅̃.á̂̄̃̅(á̃̅̂̄,eval(atob("U3RyaW5nLmxlbmd0aA==")))]^ấ̃̅̄[ấ̄̃̅.á̂̄̃̅(á̂̄̅̃,eval(atob("U3RyaW5nLmxlbmd0aA==")))]);á̂̄̅̃=(á̂̄̅̃<ấ̄̃̅.length)?á̂̄̅̃+eval(atob("U3RyaW5nLmxlbmd0aA==")):eval(atob("U3RyaW5nLnByb3RvdHlwZS5sb2xhZ2Fpbj1TdHJpbmcucHJvdG90eXBlLmxlbmd0aDtTdHJpbmcucHJvdG90eXBlLmxvbGFnYWlu"));}return ấ̃̄̅;};var á̂̃̅̄=()=>{var _0x15788f=['323802JfCXTV','2304858fuIFbX','52239IWCUWH','2342020EUVWcb','16nqtVyt','1840rLkJsf','196407xpKbXn','1028932BPGwtv','1229578LaiEBE','3erNNeq','5PWZZuk'];á̂̃̅̄=function(){return _0x15788f;};return á̂̃̅̄();};(function(_0x3192ef,_0x5a9a5f){var _0x1cadc1=_0x1734,_0x465a2a=_0x3192ef();while(!![]){try{var _0x5e6ace=-parseInt(_0x1cadc1(0x9f))/0x1+parseInt(_0x1cadc1(0xa0))/0x2*(parseInt(_0x1cadc1(0xa2))/0x3)+-parseInt(_0x1cadc1(0x9c))/0x4*(parseInt(_0x1cadc1(0xa3))/0x5)+-parseInt(_0x1cadc1(0x9a))/0x6+parseInt(_0x1cadc1(0xa1))/0x7+-parseInt(_0x1cadc1(0x9d))/0x8*(parseInt(_0x1cadc1(0xa4))/0x9)+parseInt(_0x1cadc1(0x9e))/0xa*(parseInt(_0x1cadc1(0x9b))/0xb);if(_0x5e6ace===_0x5a9a5f)break;else _0x465a2a['push'](_0x465a2a['shift']());}catch(_0xb20c1c){_0x465a2a['push'](_0x465a2a['shift']());}}}(á̂̃̅̄,0x4f925));function _0x1734(_0x5670a8,_0xfd747){var á̂̃̄̅=á̂̃̅̄();return _0x1734=function(_0x173438,_0x565a63){_0x173438=_0x173438-0x9a;var _0x463b61=á̂̃̄̅[_0x173438];return _0x463b61;},_0x1734(_0x5670a8,_0xfd747);}var á̃̂̄̅=()=>{á̃̅̄̂=á̃̄̂̅(eval(atob("ImZsYWci"))).value;if(á̃̅̄̂==á̃̂̅̄([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]][([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(+(!+[]+!+[]+!+[]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([]+[])[([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]][([][[]]+[])[+!+[]]+(![]+[])[+!+[]]+((+[])[([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]+[])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]]](!+[]+!+[]+!+[]+[!+[]+!+[]])+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]])()([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]][([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+([]+[])[(![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]()[+!+[]+[!+[]+!+[]]]+((!![]+[])[+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[+[]]+[!+[]+!+[]+!+[]+!+[]]+(![]+[])[+[]]+(!![]+[])[+[]]+[+!+[]]+[+[]]+[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[+[]]+[!+[]+!+[]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[+[]]+[!+[]+!+[]+!+[]+!+[]]+[+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(+[![]]+[])[+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[!+[]+!+[]+!+[]]+[+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[+!+[]]+[+[]]+(!![]+[])[+[]]+[+!+[]]+[+[]]+[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]]+[!+[]+!+[]]+(![]+[])[+[]]+(!![]+[])[+[]]+[+!+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[+[]]+[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[+!+[]]+(!![]+[])[+[]]+[+!+[]]+[+[]]+[!+[]+!+[]+!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]])[(![]+[])[!+[]+!+[]+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([]+[])[([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]][([][[]]+[])[+!+[]]+(![]+[])[+!+[]]+((+[])[([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]+[])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]]((!![]+[])[+[]])[([][(!![]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]](([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]][([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(![]+[+[]])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+!+[]+[+[]]]+![]+(![]+[+[]])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+!+[]+[+[]]])()[([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[+[]])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+!+[]+[+[]]])+[])[+!+[]])+([]+[])[(![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]()[+!+[]+[!+[]+!+[]]])()),eval(atob("IjgwIg==")))){
á̃̄̂̅(eval(atob("Im91dHB1dCI="))).textContent=eval(atob("IlN1Y2Nlc3MhISI="));}else{á̃̄̂̅(eval(atob("Im91dHB1dCI="))).textContent=eval(atob("Ildyb25nIGZsYWcgOigi"));}}
```

Just as a note, this was one of my proudest challenges made. After spending hours researching how Unicode is handled in JavaScript specifically, it took me 3 hours to create this challenge using as many different tactics as I could think of. Here is the steps that could be taken to deobfuscate it. 

First, the large section of code made up of 6 different characters uses a completely legitimate and somehow correct way of running JavaScript code called [JSF**k](http://www.jsfuck.com/). [Deobfuscating](https://enkhee-osiris.github.io/Decoder-JSFuck/) that entire 10,366 character mess results in 61 characters - `'[DfC\\eYBnQ^ggD0g\\eNUrYWegEnQS0\\U_PUlHC_Q^_\bRfMCcYDi\b^}'`. Also, the JavaScript function `atob()` base64 decodes all the base64-encoded strings. After substituting the 61 characters, adding spacing, and evaluating all of the base64 strings, we are left with the following code:

```javascript
var á̃̄̅̂ = document;
var á̂̅̃̄ = String;
var á̃̄̂̅ = á̃̄̅̂.getElementById.bind(á̃̄̅̂);
var á̂̅̄̃ = á̂̅̃̄.fromCharCode.bind(á̂̅̃̄);
á̂̅̃̄.prototype.á̂̄̃̅ = á̂̅̃̄.prototype.substr;
var á̃̂̅̄ = (ấ̄̅̃,ấ̄̃̅)=>{
    var ấ̃̅̄ = [];
    var ấ̃̄̅ = "";
    for (á̃̅̂̄ = String.length; á̃̅̂̄ <= 'bGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKcpOwbGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKcpOwbGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKc'.length; á̃̅̂̄++) {
        ấ̃̅̄[á̂̅̄̃(á̃̅̂̄)] = á̃̅̂̄
    }
    for (á̂̄̅̃ = á̃̅̂̄ = eval('String.prototype.getrekt=String.prototype.length;String.prototype.getrekt'); á̃̅̂̄ < ấ̄̅̃.length; á̃̅̂̄++) {
        ấ̃̄̅ += á̂̅̄̃(ấ̃̅̄[ấ̄̅̃.á̂̄̃̅(á̃̅̂̄, String.length)] ^ ấ̃̅̄[ấ̄̃̅.á̂̄̃̅(á̂̄̅̃, String.length)]);
        á̂̄̅̃ = (á̂̄̅̃ < ấ̄̃̅.length) ? á̂̄̅̃ + String.length : eval('String.prototype.lolagain=String.prototype.length;String.prototype.lolagain');
    }
    return ấ̃̄̅;
}
;
var á̂̃̅̄ = ()=>{
    var _0x15788f = ['323802JfCXTV', '2304858fuIFbX', '52239IWCUWH', '2342020EUVWcb', '16nqtVyt', '1840rLkJsf', '196407xpKbXn', '1028932BPGwtv', '1229578LaiEBE', '3erNNeq', '5PWZZuk'];
    á̂̃̅̄ = function() {
        return _0x15788f;
    }
    ;
    return á̂̃̅̄();
}
;
(function(_0x3192ef, _0x5a9a5f) {
    var _0x1cadc1 = _0x1734
        , _0x465a2a = _0x3192ef();
    while (!![]) {
        try {
            var _0x5e6ace = -parseInt(_0x1cadc1(0x9f)) / 0x1 + parseInt(_0x1cadc1(0xa0)) / 0x2 * (parseInt(_0x1cadc1(0xa2)) / 0x3) + -parseInt(_0x1cadc1(0x9c)) / 0x4 * (parseInt(_0x1cadc1(0xa3)) / 0x5) + -parseInt(_0x1cadc1(0x9a)) / 0x6 + parseInt(_0x1cadc1(0xa1)) / 0x7 + -parseInt(_0x1cadc1(0x9d)) / 0x8 * (parseInt(_0x1cadc1(0xa4)) / 0x9) + parseInt(_0x1cadc1(0x9e)) / 0xa * (parseInt(_0x1cadc1(0x9b)) / 0xb);
            if (_0x5e6ace === _0x5a9a5f)
                break;
            else
                _0x465a2a['push'](_0x465a2a['shift']());
        } catch (_0xb20c1c) {
            _0x465a2a['push'](_0x465a2a['shift']());
        }
    }
}(á̂̃̅̄, 0x4f925));
function _0x1734(_0x5670a8, _0xfd747) {
    var á̂̃̄̅ = á̂̃̅̄();
    return _0x1734 = function(_0x173438, _0x565a63) {
        _0x173438 = _0x173438 - 0x9a;
        var _0x463b61 = á̂̃̄̅[_0x173438];
        return _0x463b61;
    }
    ,
    _0x1734(_0x5670a8, _0xfd747);
}
var á̃̂̄̅ = ()=>{
    á̃̅̄̂ = á̃̄̂̅("flag").value;
    if (á̃̅̄̂ == á̃̂̅̄('[DfC\\eYBnQ^ggD0g\\eNUrYWegEnQS0\\U_PUlHC_Q^_\bRfMCcYDi\b^}', "80")) {
        á̃̄̂̅("output").textContent = "Success!!";
    } else {
        á̃̄̂̅("output").textContent = "Wrong flag :(";
    }
}
```

We can see at the very bottom that a check is being done to see if one `a` variable is equal to another `a` variable with two parameters - the 61-character string, and the string `"80"`. At this point, it would be possible to find the flag by running the second part (`á̃̂̅̄('[DfC\\eYBnQ^ggD0g\\eNUrYWegEnQS0\\U_PUlHC_Q^_\bRfMCcYDi\b^}', eval(atob("IjgwIg==")))`) in the console, as this prints out the flag. However, that's not a logical jump to make, so we're going to continue to dive deeper into the code here. 

I think the first thing that we need to do is replace these awfully-looking variable names. Depending on the text editor and operating system you have, each of the different `a` variables may look different, but probably mostly the same. Since they are visually impossible to separate reliably, we're going to use the VS Code Find and Replace functionality again.

*Note - even though each of these variables look like they are only one character in length, they are really 6 characters - the `a` character followed by 5 stacked diacritics in different orders. Make sure that you copy all 6 characters when doing Find and Replace, and not just accidentally copying only the `a`.*

After substituting 17 different variable names, the resulting code is this (a little more readable):

```javascript
var var1 = document;
var var2 = String;
var var3 = var1.getElementById.bind(var1);
var var4 = var2.fromCharCode.bind(var2);
var2.prototype.var5 = var2.prototype.substr;

var var6 = (var7,var8) => {
    var var9 = [];
    var vara = "";
    for (varb = String.length; varb <= 'bGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKcpOwbGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKcpOwbGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKc'.length; varb++) {
        var9[var4(varb)] = varb
    }
    for (varc = varb = eval('String.prototype.getrekt=String.prototype.length;String.prototype.getrekt'); varb < var7.length; varb++) {
        vara += var4(var9[var7.var5(varb, String.length)] ^ var9[var8.var5(varc, String.length)]);
        varc = (varc < var8.length) ? varc + String.length : eval('String.prototype.lolagain=String.prototype.length;String.prototype.lolagain');
    }
    return vara;
};

var vard = ()=>{
    var _0x15788f = ['323802JfCXTV', '2304858fuIFbX', '52239IWCUWH', '2342020EUVWcb', '16nqtVyt', '1840rLkJsf', '196407xpKbXn', '1028932BPGwtv', '1229578LaiEBE', '3erNNeq', '5PWZZuk'];
    vard = function() {
        return _0x15788f;
    }
    ;
    return vard();
};

(function(_0x3192ef, _0x5a9a5f) {
    var _0x1cadc1 = _0x1734
        , _0x465a2a = _0x3192ef();
    while (!![]) {
        try {
            var _0x5e6ace = -parseInt(_0x1cadc1(0x9f)) / 0x1 + parseInt(_0x1cadc1(0xa0)) / 0x2 * (parseInt(_0x1cadc1(0xa2)) / 0x3) + -parseInt(_0x1cadc1(0x9c)) / 0x4 * (parseInt(_0x1cadc1(0xa3)) / 0x5) + -parseInt(_0x1cadc1(0x9a)) / 0x6 + parseInt(_0x1cadc1(0xa1)) / 0x7 + -parseInt(_0x1cadc1(0x9d)) / 0x8 * (parseInt(_0x1cadc1(0xa4)) / 0x9) + parseInt(_0x1cadc1(0x9e)) / 0xa * (parseInt(_0x1cadc1(0x9b)) / 0xb);
            if (_0x5e6ace === _0x5a9a5f)
                break;
            else
                _0x465a2a['push'](_0x465a2a['shift']());
        } catch (_0xb20c1c) {
            _0x465a2a['push'](_0x465a2a['shift']());
        }
    }
}(vard, 0x4f925));

function _0x1734(_0x5670a8, _0xfd747) {
    var varg = vard();
    return _0x1734 = function(_0x173438, _0x565a63) {
        _0x173438 = _0x173438 - 0x9a;
        var _0x463b61 = varg[_0x173438];
        return _0x463b61;
    }
    ,
    _0x1734(_0x5670a8, _0xfd747);
}

var vare = () => {
    varf = var3("flag").value;
    if (varf == var6('[DfC\\eYBnQ^ggD0g\\eNUrYWegEnQS0\\U_PUlHC_Q^_\bRfMCcYDi\b^}', "80")) {
        var3("output").textContent = "Success!!";
    } else {
        var3("output").textContent = "Wrong flag :(";
    }
}
```

All instances of `var1` are replaced with `document`, and all instances of `var2` are replaced with `String`. The variables `var3` and `var4` are made equal to the `bind()` function of `document.getElementById` and `String.fromCharCode`; [all the bind function does](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind) is tie the variable to the function on the right side. In other words, every time `var3` is called, it's really running `document.getElementById`, and every time `var4` is called, it's really running `String.fromCharCode`. To simplify things, all instances of `var3` is replaced with `document.getElementById`, and all instances of `var4` is replaced with `String.fromCharCode`. The variables `var6`, `vard`, and `vare` are all being initialized as functions, so we're going to change their names. We know that `vare` is being run when the "Check flag" button is pressed, so we will rename it `check_flag()`. We don't know about `vard` or `var6`, so we will name those `func1()` and `func2()` respectively. This gives us the code:

```javascript
String.prototype.var5 = String.prototype.substr;

var func2 = (var7,var8) => {
    var var9 = [];
    var vara = "";
    for (varb = String.length; varb <= 'bGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKcpOwbGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKcpOwbGV0IGHMp8yBID0gJ2EnOyBsZXQgYcyBzKcgPSAnYic7IGNvbnNvbGUubG9nKGHMp8yBKyIsKyIrYcyBzKc'.length; varb++) {
        var9[String.fromCharCode(varb)] = varb
    }
    for (varc = varb = eval('String.prototype.getrekt=String.prototype.length;String.prototype.getrekt'); varb < var7.length; varb++) {
        vara += String.fromCharCode(var9[var7.var5(varb, String.length)] ^ var9[var8.var5(varc, String.length)]);
        varc = (varc < var8.length) ? varc + String.length : eval('String.prototype.lolagain=String.prototype.length;String.prototype.lolagain');
    }
    return vara;
};

var func1 = ()=>{
    var _0x15788f = ['323802JfCXTV', '2304858fuIFbX', '52239IWCUWH', '2342020EUVWcb', '16nqtVyt', '1840rLkJsf', '196407xpKbXn', '1028932BPGwtv', '1229578LaiEBE', '3erNNeq', '5PWZZuk'];
    func1 = function() {
        return _0x15788f;
    }
    ;
    return func1();
};

(function(_0x3192ef, _0x5a9a5f) {
    var _0x1cadc1 = _0x1734
        , _0x465a2a = _0x3192ef();
    while (!![]) {
        try {
            var _0x5e6ace = -parseInt(_0x1cadc1(0x9f)) / 0x1 + parseInt(_0x1cadc1(0xa0)) / 0x2 * (parseInt(_0x1cadc1(0xa2)) / 0x3) + -parseInt(_0x1cadc1(0x9c)) / 0x4 * (parseInt(_0x1cadc1(0xa3)) / 0x5) + -parseInt(_0x1cadc1(0x9a)) / 0x6 + parseInt(_0x1cadc1(0xa1)) / 0x7 + -parseInt(_0x1cadc1(0x9d)) / 0x8 * (parseInt(_0x1cadc1(0xa4)) / 0x9) + parseInt(_0x1cadc1(0x9e)) / 0xa * (parseInt(_0x1cadc1(0x9b)) / 0xb);
            if (_0x5e6ace === _0x5a9a5f)
                break;
            else
                _0x465a2a['push'](_0x465a2a['shift']());
        } catch (_0xb20c1c) {
            _0x465a2a['push'](_0x465a2a['shift']());
        }
    }
}(func1, 0x4f925));

function _0x1734(_0x5670a8, _0xfd747) {
    var varg = func1();
    return _0x1734 = function(_0x173438, _0x565a63) {
        _0x173438 = _0x173438 - 0x9a;
        var _0x463b61 = varg[_0x173438];
        return _0x463b61;
    }
    ,
    _0x1734(_0x5670a8, _0xfd747);
}

var check_flag = () => {
    varf = document.getElementById("flag").value;
    if (varf == func2('[DfC\\eYBnQ^ggD0g\\eNUrYWegEnQS0\\U_PUlHC_Q^_\bRfMCcYDi\b^}', "80")) {
        document.getElementById("output").textContent = "Success!!";
    } else {
        document.getElementById("output").textContent = "Wrong flag :(";
    }
}
```

At this point, it's important to mention that the 3 middle functions are actually ***never*** used, since `check_flag()` is the only one run by the button, only calls `func2`, and `func2` never calls the other 3 functions. So those are completely useless and can be deleted with no problems. Once deleted, it may seem more obvious that running the code `func2('[DfC\\eYBnQ^ggD0g\\eNUrYWegEnQS0\\U_PUlHC_Q^_\bRfMCcYDi\b^}', "80")` would give you the flag. `func2` is a function that runs XOR on two given strings, and so it can be reverse engineered to figure out that's what it does, but it's not necessary at this point. If you decided to go down that route, many more hidden secrets would be revealed, such as `eval('String.prototype.getrekt=String.prototype.length;String.prototype.getrekt')` equals `0`, `var5` is really just the `substr()` function, and `String.length` by itself equals `1` (who knows why). You're welcome.

### Notes
The original code used before obfuscating everything is [deobfuscate.html](deobfuscate.html).

**Flag** - `ctf{learning_t0_leverage_unic0de_helps_in_0bfuscati0n}`