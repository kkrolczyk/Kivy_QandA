# Kivy_QandA
my Kivy gotcha's [Python]



1. Any class defined in \*.kv file must have 'forward declaration' in \*.py (demo somewhat in code)

2. Two main ideas for accessing kv <=> py:

  a) either via {Object|String|...}Property in both kv/py
  b) or via root.ids.id\_object1\_name.id\_object2\_name.property  (TODO:example)

3. Prevent having item/button/object fill whole Layout, plus Popup usage demo (demo in code)

4. If I want Label/Button that does not get overflown but scrolls/wraps it's contents (demo in code)

5. Using screens and Screen manager, and handling keys that Window receives

6. Detecting Android window size or orientation - no idea... (TODO:find simple method)

7. Using KV builder class from Python code (demo in code)

8. Remember about textwrap.dedent :)



