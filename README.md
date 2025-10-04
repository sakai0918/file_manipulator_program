# File manipulator program
指定されたテキストファイルを読み込み、コマンドによってファイル操作します。

# 使い方
以下それぞれの場合に合わせてコマンドを入力してください。
テキストファイルの拡張子は`.txt`である必要があります。

-読み込んだ内容を逆にして別のテキストファイルに出力  
`python3 file_manipulator.py reverse [入力テキストファイル]　[出力テキストファイル]`

-読み込んだ内容を別のテキストファイルに出力  
`python3 file_manipulator.py copy [入力テキストファイル]　[出力テキストファイル]`

-読み込んだ内容を指定した回数だけ複製して同じファイルに出力  
`python3 file_manipulator.py duplicate-contents [テキストファイル]`

-読み込んだ内容のうち指定した文字列を別の文字列に置き換えて同じファイルに出力  
`python3 file_manipulator.py [テキストファイル] [置換前の文字列] [置換後の文字列]`
