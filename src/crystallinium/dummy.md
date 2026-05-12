# Heading 1 — dummy parser test

This is a dummy Markdown file to test the Markdown parser. It contains basic text, headers, lists, code blocks, links, images, quotes, bold, italic, inline code, and attribution formatting.

## Heading 2 — text and emphasis

This is a plain paragraph with **bold text**, *italic text*, and ***bold italic text*** inline.

This is a paragraph with `inline code`, ``double-backtick inline code``, and a raw error: `Uncaught ReferenceError: 'x' is not defined`.

This sentence has a hard line break trailing two spaces.  
This is the line after the hard break.

This is a new paragraph after a blank line.

This is a sentence with a comment:

The quick brown fox jumps over the lazy dog. <!-- This is a comment that should be ignored by the parser. -->

## Heading 3 — lists

- This is an unordered list item.
  - This is a nested unordered list item.
    - This is an even more nested list item!!
- Another unordered list item.
- A third unordered list item.

1. This is an ordered list item.
2. This is a second ordered list item.
   1. This is a nested ordered list item.
   2. Another nested ordered list item.
3. Back to top level.

- Mixed nesting test:
  - Unordered child.
    1. Ordered grandchild.
    2. Another ordered grandchild.
  - Back to unordered child.

- This is a list mixing dash and star bullet points.
* This is a list mixing dash and star bullet points.
* Let's hope the parser doesn't crash with a `Traceback (most recent call last)`.

### Heading 3 — blockquotes

> The pain of today is the strength of tomorrow.

> Nested quote level one.
>> Nested quote level two.
>>> Nested quote level three.

> A blockquote with **bold** and *italic* and `inline code` inside it.

> A multiline blockquote.
> This is still the same quote block.
> Still going.

There is a trailing newline hidden behind this quote block.

### Heading 3 — code blocks

```latex
10! = 3628800
```

```python
def fact(n) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def perm(n, r) -> int:
    return fact(n) / fact(n - r)

def choose(n, r) -> int:
    return perm(n, r) / fact(r)

try:
    raise TypeError("This is an error.")
except TypeError as e:
    print("We caught the TypeError:", e)
```

```log
[2024-06-01 12:00:00] INFO: Starting the application...
[2024-06-01 12:00:01] WARN: Database connection error. Please check your network settings.
[2024-06-01 12:00:01] DEBUG: Initialising modules...
[2024-06-01 12:00:02] ERROR: Failed to connect to database: Connection refused
[2024-06-01 12:00:03] INFO: Shutting down the application.
[2024-06-01 12:00:04] FATAL: Application terminated unexpectedly due to an unhandled exception.

zsh: segmentation fault: python3
Command executed in 620ms and failed (exit code 139)

git: fatal: unable to access 'https://github.com/user/badrepo.git': Could not resolve host: github.com
```

```log
You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false
```

```
This is a code block with no language tag.
It should not apply syntax highlighting.
It should preserve    spacing and
	tabs.
```

Btw, Python does not like these: '	'. These are tabs, Python will slap you in the face with a `TabError: inconsistent use of tabs and spaces in indentation` if you try to run code with tabs in it. Always use spaces for indentation in Python!

```python
# Edge case: code block immediately followed by another code block.
x = 1
```

```python
y = 2
```

## Heading 2 — links and images

This is a [basic link](https://example.com).

This is a [link with a title](https://example.com "Example Domain").

This is a bare URL: https://example.com

This is an ![alt text](https://example.com/image.png) inline image.

This is a [reference-style link][ref1].

[ref1]: https://example.com "Reference Link"

## Heading 2 — attribution syntax

> *"You just want attention, you don't want my heart. Maybe you just hate the thought of me with someone new. Yeah, you just want attention, I knew from the start. You're just making sure I'm never getting over you"*
> — **Charlie Puth**

> *IT'S SHOWTIME*
> — **Arnold Schwarzenegger**  
> *You have been terminated*
> — **Arnold Schwarzenegger**  
> *Get to the choppa!*
> — **Arnold Schwarzenegger**  
> *Hasta la vista, baby.*
> — **Arnold Schwarzenegger**

> *HAI 1.2, CAN HAS STDIO?*
> — **Grumpy Cat**

> *"Why did the chicken cross the road? Because it wanted to get to the other side."*
> — **(It's a joke as old as time itself)**

Block Quote Raw HTML
<blockquote>
  "I CAN HAS CHEEZBURGER?"
  <footer>— <cite>Grumpy Cat</cite></footer>
</blockquote>

> *KTHXBYE*
> – **"Grumpy Cat"**

## Heading 2 — boolean glyphs

Testing Meme Parsing:

Python:  
✅ brew install  
✅ saves you time  
✅ free forever  
✅ Traceback (most recent call last)  
✅ always one command away  

Girlfriend:  
❌ extremely hard to get  
❌ wastes your time  
❌ spends all your money  
❌ doesn't tell you what's wrong  
❌ breaks up with you  

## Heading 2 — horizontal rules

---

***

___

## Heading 2 — edge cases

**This bold span is not closed.

*This italic span is not closed.

`This inline code is not closed.

This is a paragraph with an \*escaped asterisk\* and a \`escaped backtick\`.

This paragraph has a [broken link](with no closing paren.

This paragraph has an empty link []().

This paragraph has a link with no text [](https://example.com).

    This is an indented code block via four spaces.
    It should be treated as a code block.
    No language tag.

This line ends with trailing whitespace.   

> 
> This blockquote has an empty line inside it.
>

## Heading 2 — long-form prose

Python is a high-level, imperative, object-oriented programming language that emphasises code readability and simplicity. It was created by Guido van Rossum in 1991 and has since become one of the most popular programming languages in the world.

GitHub is an open-source platform for version control and collaboration. It allows developers to host their projects online and collaborate with others using a web-based interface or command-line tools.

The Pigeonhole Principle states that if *n* items are placed into *m* containers, and *n* > *m*, then at least one container must hold more than one item. It is used extensively in combinatorics and computer science.

The alternate segment theorem states that the angle between a tangent to a circle and a chord drawn from the point of tangency is equal to the inscribed angle on the opposite side of the chord. Formally: if **α** is the angle between tangent *t* and chord *TP*, then **α** equals the inscribed angle in the alternate segment.

Tybalt's Death (Act 3, Scene 1 of *Romeo and Juliet*) was a significant event in the play. For what reason? I can't remember, lol.

## Heading 2 — empty and degenerate cases

##Heading with no space after hashes

###### Heading 6

####### This has too many hashes and should not be a heading.

- 
- Empty list item above.

1. 
2. Empty ordered list item above.

> 

Empty blockquote above.

``````
Triple-nested backtick fence edge case.
``````

This is the last line of the file with no trailing newline.