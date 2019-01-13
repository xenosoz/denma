# Denma
Replace sed for the simplest use cases.
[https://github.com/xenosoz/denma](https://github.com/xenosoz/denma)

It's in quick and dirty MVP state for the personal use.
Ping me if you think we need to improve this seriously.

## Background
We have three slashes in "s/old/new/command" the perl-style replacement format.
That means we need to escape slashes every time we want to use in the old, new and command section.
I am tired of it. But I'm lucky enough to have python within my era.

*Update: We learn sed is capable of changing its delimiter. See [Back to sed](#back-to-sed) section below.*

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

## Back to sed
After creating this project, we got a feedback from @ehooi. We really appreciate it. We might still stick to sed:
```
sed 's#a/very/old/and/long/path#new/path#g' -i input.txt
```

We can also use any character but a backslash or newline as a delimiter. Two references here:
- [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.txt):
"The '%' may be replaced by any other single character."
- [Freebsd sed manual](https://man.freebsd.org/sed):
"Any character other than a backslash or newline can be used instead of a slash ..."


## License
[MIT License](https://opensource.org/licenses/MIT) as per [LICENSE.md](LICENSE.md).

## Credits
Created by Taihyun Hwang &lt;xenosoz.hwang@gmail.com&gt;

