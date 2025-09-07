## READ ME NUMB3RS.py

This program checks if a given string is a proper IPv4 address. Nothing fancy, just catching bad inputs before they embarrass you on the network.

## How it works
• Takes input like “192.168.0.1”.
• Splits it by dots. If there aren’t exactly four parts, it’s out.
• Each part must be all digits, between 0 and 255, and not padded with zeros (so “01” is kicked out).
• If everything passes, it prints True. Otherwise, False.

## How I solved it
Started by splitting on the dot and counting the pieces. 
Then one paranoid check after another: is it digits, right length, right range, no sneaky leading zeros. A little over-defensive, but safer than letting 999.888.777.666 call itself an IP.

## Questions I asked myself
– Is “0.0.0.0” valid? Yes.
– Is “255.255.255.255”? Also yes.
– Do I care about addresses reserved for networks or broadcast? No, out of scope.
– Should “1.2.3.04” pass? No, the leading zero test shuts that down.

## Examples
Input: 192.168.1.1 -> Output: True
Input: 256.100.50.25 -> Output: False
Input: cats.are.not.ips -> Output: False

## Signature
// Kimberley B.