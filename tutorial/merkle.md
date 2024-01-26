# Merkle Trees, Merkle Sum Trees and "Broken" Merkle Sum Trees

# What are Merkle Trees
Merkle trees are a logical way of storing data in an organised structure. In specidic a tree-like structure is used, where the bottom most layers contain actual data eg. Account balances. 

As we traverse the tree structure from the bottom to the top of the tree, each leaf is hashed with it's sibling to generate a hash value representing the data held by the two sibling nodes. 

An example of this would be a below:
| | | | | | | | | |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| | | | | Root Hash is the hash value of HASH(Level1 LHS,Level1 RHS) | | | | |
| | | | Level1 Lefthand side Hash is the hash value of HASH(Level2 Value1,Level1 Value2)| | Level1 Righthand Hash side is the hash value of HASH(Level2 Value3,Level2 Value4)| | | |
| |Level2 Value1 | | Level2 Value2 | | Level2 Value3 | | Level2 value4 | |

