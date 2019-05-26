

import tkinter as tk
import random
import six
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements
window=tk.Tk()
window.title('苏联笑话生成器')
window.geometry('600x700')


def shenchen():
    t.delete('1.0','end')
    var1=v1.get()
    var2=v2.get()
    var3=v3.get()
    var4=v4.get()
    var5=v5.get()
    a = random.randint(1,19)
    if a==1:
        var=var2+':“由于'+var1+'的实行，各位'+var4+'的美好未来前景已经出现在了地平线上。”'+'\n\n'+'一个'+var4+'问另一个'+var4+':”什么是地平线?”\n\n另一个'+var4+'回答道:“就是那个能看到但是永远都到不了的线。”'
    elif a==2:
        var='问：“'+var1+'的前景是什么？”\n\n答：“有两种可能的情况。现实的可能是火星人会降临地球帮我们打理一切，科幻的可能是我们成功地'+var3+'。”'
    elif a==3:
        var='在'+var5+'庆典的聚会上，一位35岁的'+var4+'高举着牌子，上面写着“感谢'+var1+'赐予我的快乐的童年”。\n\n'+var2+'呵斥道，“你是在嘲讽'+var1+'吗？'+var1+'才实行了20年。”\n\n“确切地说，这正是我感谢它的原因。”'
    elif a==4:
        var=var2+'的汽车被一头牛挡住了，怎么也赶不走。'+var2+'便下车对牛说：“你再不走，我就把你送到'+var5+'去'+var1+'。”牛听了便一溜烟的跑开了。'
    elif a==5:
        var=var2+'发言道：“从下个礼拜开始我们要做两件事，一，全面在'+var5+'实行'+var1+'；二，周六所有'+var4+'都要去酒吧里拿一条蜥蜴。大家有什么意见可以提出来。”\n\n过了一会儿，台下有个声音怯生生地提问：“为什么要拿蜥蜴？”\n\n“很好，我就知道大家对'+var1+'没有异议。”'
    elif a==6:
        var='“'+var1+'真**的智障！”\n\n“你涉嫌恶意攻击'+var2+',跟我走一趟。”\n\n“我又没说是哪里的'+var1+'！”\n\n“废话！哪里的'+var1+'智障我会不知道吗！”'
    elif a==7:
        var='问：“'+var1+'的优越之处是什么？”\n\n答：“成功克服了那些其他情况下不会存在的困难。”'
    elif a==8:
        var='问：“'+var1+'在哪些时候会遇到抵制？”\n\n答：“主要有四个时间段：春天、夏天、秋天和冬天。”'
    elif a==9:
        var='问：“'+var1+'实行的结果如何？”\n\n答：“还是有人活下来了。”'
    elif a==10:
        var=var2+'问一名'+var4+':“你的爸爸是谁？”\n\n他回答说：“是'+var2+'!”\n\n'+var2+'很满意，又问：“你的母亲是谁？”\n\n他回答：“是'+var1+'！”\n\n'+var2+'又问：“你将来想当什么？”\n\n“孤儿！”'
    elif a==11:
        var='问：“什么是最短的笑话？”\n\n答：“'+var1+'。”'
    elif a==12:
        var='“'+var1+'是艺术还是科学?”\n\n”我说不好，但肯定不是科学。”\n\n“何以见得?”\n\n“如果'+var1+'是科学的话，他们至少应该先用小白鼠做实验。”'
    elif a==13:
        var=var2+'在'+var5+'随机采访了一位'+var4+':“请问你对'+var1+'有什么意见吗?”\n\n'+var4+'答道:“我有一些意见，但我不同意我的意见!”'
    elif a==14:
        var=var2+'在向'+var4+'们讲话：\n\n“很快我们就能3！”\n\n台下传来一个声音：“那我们怎么办？”'
    elif a==15:
        var='问：“什么叫交换意见？”\n\n答：“带着你的意见去找'+var2+'理论，然后带着他的回来。”'
    elif a==16:
        var='“如果你在'+var5+'，旁边一个陌生人突然开始唉声叹气，正确的做法是什么?”\n\n“立即阻止这种反对'+var1+'的行为。”'
    elif a==17:
        var=var2+':“我们要不惜一切代价，为了我们的主人翁'+var3+'！”\n\n一个'+var4+'对另一个'+var4+'说:“看哪 ，'+var2+'把咱们当主人翁。”\n\n另一个'+var4+'说:“不，我们是‘代价’。”'
    elif a==18:
        var='问：“为什么'+var2+'把'+var4+'放在中心考虑？”\n\n答：“这样从各个方向都能方便地欺压他们。”'
    elif a==19:
        var='两个骷髅相遇，一骷髅问另一个骷髅:“我是被'+var2+'的'+var1+'逼死的，你是怎么死的？”\n\n另一个骷髅回答说:“我还活着。”'

 


   
    t.insert('insert',var)
def insert_end():
    var=e.get()
    t.insert('end',var)
#这里的end表示插入在结尾，可以换为1.2，则插入在第一行第二位后面
'''
ft3=tk.font.Font(size=14)
ft4=tk.font.Font(size=12)
'''
tk.Label(text='要讽刺的事情是？：').pack()
global v1
v1=tk.StringVar()
tk.Entry(width=30,textvariable=v1,bg='Ivory').pack()
         
tk.Label(text='这件事是谁提出来的？：').pack()
global v2
v2=tk.StringVar()
tk.Entry(width=30,textvariable=v2,bg='Ivory').pack()
         
tk.Label(text='提出者声称这件事有助于什么？：').pack()
global v3
v3=tk.StringVar()
tk.Entry(width=30,textvariable=v3,bg='Ivory').pack()
         
tk.Label(text='这件事针对的是哪些人？：').pack()
global v4
v4=tk.StringVar()
tk.Entry(width=30,textvariable=v4,bg='Ivory').pack()
         
tk.Label(text='这件事起作用的范围？：').pack()
global v5
v5=tk.StringVar()
tk.Entry(width=30,textvariable=v5,bg='Ivory').pack()

b1=tk.Button(window,text='生成笑话！',width=15,height=2,command=shenchen)
b1.pack()

t=tk.Text(window,height=10)     #这里设置文本框高，可以容纳两行
t.pack()

tk.Label(text='宣同学没事瞎写的，不对生成器的任何言论负责。（假装这有个滑稽的表情）').pack()

window.mainloop()

