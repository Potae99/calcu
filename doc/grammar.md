# Grammar for the calculator

## Operator Precedence
| Precedence | Operators | Associativity |
| ---------- | --------- | ------------- |
|     0      |     (     | Right to Left |
|     1      |      !    | Left to Right |
|     2      |      ^    | Right to Left |
|     3      | Unary -/+ | Right to Left |
|     4      | *, /, %   | Left to Right |
|     5      |    +, -   | Left to Right |

## Version 0 (Number)
The arithmetic expression is only a number.

```
Arithmetic Expression (AE) = Number
```

## Version 1: Factorial
Add the factorial expression.

```
Arithmetic Expression (AE) = FactExpr
FactExpr = Number {"!"}

```

## Version 2: Power
Add the power expression.

```
Arithmetic Expression (AE) = PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Number {"!"}

```

## Version 3: Unary
Add the unary -/+ expression.

```
Arithmetic Expression (AE) = UnaryExpr
UnaryExpr = ["-" | "+"] PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Number {"!"}

```
## Version 4: Multiplication
Add the multiplication expression.

```
Arithmetic Expression (AE) = MulExpr
MulExpr = UnaryExpr {("*" | "/" | "%") UnaryExpr}
UnaryExpr = ["-" | "+"] PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Number {"!"}

```
## Version 5: Addition
Add the addition expression.

```
Arithmetic Expression (AE) = AddExpr
AddExpr = MulExpr {("+" | "-") MulExpr}
MulExpr = UnaryExpr {("*" | "/" | "%") UnaryExpr}
UnaryExpr = ["-" | "+"] PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Number {"!"}

```

## Version 6: Parenthesis
Add the addition expression.

```
Arithmetic Expression (AE) = AddExpr
AddExpr = MulExpr {("+" | "-") MulExpr}
MulExpr = UnaryExpr {("*" | "/" | "%") UnaryExpr}
UnaryExpr = ["-" | "+"] PowerExpr
PowerExpr = FactExpr {"^" PowerExpr}
FactExpr = Primary {"!"}
Primary = Number | "(" AE ")"

```

## Lexical Grammar 
```
LeftParen = "("
RightParen = ")"
AddOp = "+" | "-"
MulOp = "*"| "/"| "%"
PowerOp = "^"
FacOp = "!" 
Number = Digit { Digit }
Digit = "0" | ... | "9" 

```