# Variáveis e Data Types

## String

```js
"Aqui é uma string"; 
'Aqui também é uma string';
```

## Numbers

```js
500;
3.14;
-1;
```

## Booleans

```js
false;
true;
```

```js
const var = Boolean("IFPE");
console.log(var);
```

### Especiais

 ```js
 underfined;
 null;
 NaN;
 ```

## Objects

```js
const user = {
    name: "Rodrigo", 
    username: "rodrigoclira",
};
```

## Array

```js
const users = ['Patrique', 'Roberto', 'Selma'];
const numerosSorteados = [20, 3, 10, 50];
const meuArray = ['Patrique', 20, 'Roberto', 10];

const superUsers = [
    { name: 'chris'},
    { name: 'nick' },
    { name: 'selma'},
];
```

## Criando variável

As formas de criar variável em JS são: 

```js
var thing = 'primeiro'; // Não é mais usado

const otherThing = 'segundo'; // Não pode redefinir

let newThing = 'third' // Como criar uma variável que pode ser redefinida
```

Redefinindo uma propriedade de um objeto

```js
const objetoConst = {
    name: 'rodrigo',
};

objetoConst.name = 'lira';
```

Declarando uma variável e depois adicionado um valoir

```js
let minhaVar;
minhaVar = 'algo';
```