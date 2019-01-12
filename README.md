# Denma
Replace sed for the simplest use cases.
[https://github.com/xenosoz/denma](https://github.com/xenosoz/denma)

It's in quick and dirty MVP state for the personal use.
Ping me if you think we need to improve this seriously.

## Background
We have three slashes in "s/old/new/command" the perl-style replacement format.
That means we need to escape slashes every time we want to use in the old, new and command section.
I am tired of it.

But I'm lucky enough to have python within my era.

## Details
Denma exposes a variable `line` for each line.
You can write an expression for the replacement or just update the variable the with statements.

We present three equivalent commands below:
```
sed 's/a\/very\/old\/and\/long\/path/new\/path/g' -i input.txt
```
```
denma.py -i -c "line.replace('a/very/old/and/long/path', 'new/path')" input.txt
```
```
denma.py -i -c "import re; line = re.sub('a/very/old/and/long/path', 'new/path', line)" input.txt 
```

## License
[MIT License](https://opensource.org/licenses/MIT) as per [LICENSE.md](LICENSE.md).

## Credits
Created by Taihyun Hwang &lt;xenosoz.hwang@gmail.com&gt;

