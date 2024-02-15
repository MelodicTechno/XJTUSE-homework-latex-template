# README

## 编译

用xelatex编译

## 代码

代码放到code文件夹中，推荐先将后缀名改成.txt，因为我用vscode写latex，不改后缀vscode的java插件会叫我建立项目，很烦。

在code中有用来批量改后缀的python代码，挺好用的。注意要将terminal定位到code文件夹的位置然后在terminal输入python change_file_name.py，运行。

代码中的中文（包括注释和字符串中的中文）要用``包裹起来，不然渲染代码颜色的宏包会报错，英文注释无所谓。代价是中文的注释不会被上色，暂时没想到解决办法。

在template.tex中提供了两种显示代码的方案，一种有框框一种没有，我觉得没有框框的更好看。

## 图片

文档里插入的图片在images文件夹里

## .gitiignore

我一般把编译文件的输出路径设在根目录的文件夹out里然后把out加到.gitignore里，不然一堆提示很烦。当然.gitignore里还有其他忽略git的设置

## .chktexrc

在vscode里写latex一般要用到latex-workshop插件，而用这东西写中文很经常报警，.chktexrc正式为此而设。在里面加入了一些命令来解决中文导致的警报。

## LICENSE

项目是MIT Lisense所以怎么用都无所谓。我记得甚至可以商用。不过整个项目都写得挺烂的凑合着用吧。（说得好像真的会有人用一样）
