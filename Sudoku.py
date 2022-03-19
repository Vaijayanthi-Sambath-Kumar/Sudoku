import streamlit as st
from PIL import Image
st.set_page_config(page_title="SUDOKU")
st.header("SUDOKU")
st.write('''Welcome! We offer the following difficulty levels in sudoku:
1. Easy
2. Medium
3. Hard ''')
x=st.number_input("Enter the difficulty level",1,3)
if x==1:
    image=Image.open("Easy sudoku.jpg")
    st.image(image, caption="Easy sudoku")
    st.write('''Enter the values  according to the coordinates.
For example, if you are asked the value for box (1,5), it means enter the value for the box on 1st row and 5th column.''')
    a=st.number_input("(1,1)",1,9)
    t=st.number_input("(5,1)",1,9)
    y=st.number_input("(6,1)",1,9)
    ad=st.number_input("(7,1)",1,9)
    ai=st.number_input("(8,1)",1,9)
    b=st.number_input("(1,2)",1,9)
    u=st.number_input("(5,2)",1,9)
    ae=st.number_input("(7,2)",1,9)
    an=st.number_input("(9,2)",1,9)
    C=st.number_input("(1,3)",1,9)
    e=st.number_input("(2,3)",1,9)
    j=st.number_input("(3,3)",1,9)
    o=st.number_input("(4,3)",1,9)
    z=st.number_input("(6,3)",1,9)
    aj=st.number_input("(8,3)",1,9)
    f=st.number_input("(2,4)",1,9)
    k=st.number_input("(3,4)",1,9)
    aa=st.number_input("(6,4)",1,9)
    ak=st.number_input("(8,4)",1,9)
    ao=st.number_input("(9,4)",1,9)
    l=st.number_input("(3,5)",1,9)
    p=st.number_input("(4,5)",1,9)
    v=st.number_input("(5,5)",1,9)
    ab=st.number_input("(6,5)",1,9)
    af=st.number_input("(7,5)",1,9)
    c=st.number_input("(1,6)",1,9)
    g=st.number_input("(2,6)",1,9)
    q=st.number_input("(4,6)",1,9)
    ag=st.number_input("(7,6)",1,9)
    al=st.number_input("(8,6)",1,9)
    h=st.number_input("(2,7)",1,9)
    r=st.number_input("(4,7)",1,9)
    ac=st.number_input("(6,7)",1,9)
    ah=st.number_input("(7,7)",1,9)
    am=st.number_input("(8,7)",1,9)
    ap=st.number_input("(9,7)",1,9)
    d=st.number_input("(1,8)",1,9)
    m=st.number_input("(3,8)",1,9)
    w=st.number_input("(5,8)",1,9)
    aq=st.number_input("(9,8)",1,9)
    i=st.number_input("(2,9)",1,9)
    n=st.number_input("(3,9)",1,9)
    s=st.number_input("(4,9)",1,9)
    x=st.number_input("(5,9)",1,9)
    ar=st.number_input("(9,9)",1,9)
    abc=st.number_input("Enter 1 for submitting.")
    if abc==1:
        if a==4 and b==3 and C==5 and c==9 and d==8 and e==2 and f==5 and g==1 and h==4 and i==3 and j==7 and k==8 and l==3 and m==6 and n==2 and o==6 and p==9 and q==5 and r==3 and s==7 and t==3 and u==7 and v==8 and w==1 and x==5 and y==9 and z==1 and aa==7 and ab==4 and ac==6 and ad==5 and ae==1 and af==2 and ag==6 and ah==8 and ai==2 and aj==8 and ak==9 and al==7 and am==1 and an==6 and ao==4 and ap==2 and aq==5 and ar==9:
            st.write("Correct!")
            st.balloons()
        else:
            st.write("Incorrect.... Hard luck!")
elif x==2:
    image=Image.open("Medium Sudoku.jpg")
    st.image(image, caption="Medium Level Sudoku")
    st.write('''Enter the values  according to the coordinates.
For example, if you are asked the value for box (1,5), it means enter the value for the box on 1st row and 5th column.''')
    a=st.number_input("(1,1)",1,9)
    b=st.number_input("(2,1)",1,9)
    C=st.number_input("(3,1)",1,9)
    c=st.number_input("(4,1)",1,9)
    d=st.number_input("(5,1)",1,9)
    e=st.number_input("(6,1)",1,9)
    f=st.number_input("(7,1)",1,9)
    g=st.number_input("(8,1)",1,9)
    h=st.number_input("(9,1)",1,9)
    i=st.number_input("(4,2)",1,9)
    j=st.number_input("(7,2)",1,9)
    k=st.number_input("(8,2)",1,9)
    l=st.number_input("(9,2)",1,9)
    m=st.number_input("(1,3)",1,9)
    n=st.number_input("(2,3)",1,9)
    o=st.number_input("(4,3)",1,9)
    p=st.number_input("(5,3)",1,9)
    q=st.number_input("(8,3)",1,9)
    r=st.number_input("(1,4)",1,9)
    s=st.number_input("(3,4)",1,9)
    t=st.number_input("(4,4)",1,9)
    u=st.number_input("(6,4)",1,9)
    v=st.number_input("(7,4)",1,9)
    w=st.number_input("(9,4)",1,9)
    x=st.number_input("(2,5)",1,9)
    y=st.number_input("(3,5)",1,9)
    z=st.number_input("(4,5)",1,9)
    aa=st.number_input("(6,5)",1,9)
    ab=st.number_input("(7,5)",1,9)
    ac=st.number_input("(8,5)",1,9)
    ad=st.number_input("(1,6)",1,9)
    ae=st.number_input("(3,6)",1,9)
    af=st.number_input("(4,6)",1,9)
    ag=st.number_input("(6,6)",1,9)
    ah=st.number_input("(7,6)",1,9)
    ai=st.number_input("(9,6)",1,9)
    aj=st.number_input("(2,7)",1,9)
    ak=st.number_input("(5,7)",1,9)
    al=st.number_input("(6,7)",1,9)
    am=st.number_input("(8,7)",1,9)
    an=st.number_input("(9,7)",1,9)
    ao=st.number_input("(1,8)",1,9)
    ap=st.number_input("(2,8)",1,9)
    aq=st.number_input("(3,8)",1,9)
    ar=st.number_input("(6,8)",1,9)
    at=st.number_input("(1,9)",1,9)
    au=st.number_input("(2,9)",1,9)
    av=st.number_input("(3,9)",1,9)
    aw=st.number_input("(4,9)",1,9)
    ax=st.number_input("(5,9)",1,9)
    ay=st.number_input("(6,9)",1,9)
    az=st.number_input("(7,9)",1,9)
    aaa=st.number_input("(8,9)",1,9)
    aab=st.number_input("(9,9)",1,9)
    abc=st.number_input("Enter 1 for submitting.")
    if abc==1:
        if a==8 and b==5 and C==9 and c==3 and d==1 and e==7 and f==6 and g==2 and h==4 and i==9 and j==5 and k==8 and l==3 and m==6 and n==3 and o==4 and p==8 and q==9 and r==1 and s==7 and t==6 and u==4 and v==3 and w==2 and x==9 and y==4 and z==5 and aa==3 and ab==8 and ac==1 and ad==3 and ae==5 and af==1 and ag==8 and ah==7 and ai==9 and aj==7 and ak==4 and al==1 and am==6 and an==5 and ao==4 and ap==2 and aq==8 and ar==6 and at==5 and au==1 and av==6 and aw==2 and ax==3 and ay==9 and az==4 and aaa==7 and aab==8:
            st.write("Correct!")
            st.balloons()
        else:
            st.write("Incorrect.... Hard luck!")
else:
    image=Image.open("Hard Sudoku.jpeg")
    st.image(image, caption="Hard Sudoku")
    st.write('''Enter the values  according to the coordinates.
For example, if you are asked the value for box (1,5), it means enter the value for the box on 1st row and 5th column.''')
    a=st.number_input("(3,1)",1,9)
    b=st.number_input("(4,1)",1,9)
    C=st.number_input("(6,1)",1,9)
    c=st.number_input("(7,1)",1,9)
    d=st.number_input("(9,1)",1,9)
    e=st.number_input("(1,2)",1,9)
    f=st.number_input("(2,2)",1,9)
    g=st.number_input("(4,2)",1,9)
    h=st.number_input("(5,2)",1,9)
    i=st.number_input("(8,2)",1,9)
    j=st.number_input("(9,2)",1,9)
    k=st.number_input("(1,3)",1,9)
    l=st.number_input("(4,3)",1,9)
    m=st.number_input("(7,3)",1,9)
    n=st.number_input("(9,3)",1,9)
    o=st.number_input("(2,4)",1,9)
    p=st.number_input("(4,4)",1,9)
    q=st.number_input("(5,4)",1,9)
    r=st.number_input("(6,4)",1,9)
    s=st.number_input("(7,4)",1,9)
    t=st.number_input("(9,4)",1,9)
    u=st.number_input("(1,5)",1,9)
    v=st.number_input("(3,5)",1,9)
    w=st.number_input("(5,5)",1,9)
    x=st.number_input("(6,5)",1,9)
    y=st.number_input("(7,5)",1,9)
    z=st.number_input("(9,5)",1,9)
    aa=st.number_input("(1,6)",1,9)
    ab=st.number_input("(3,6)",1,9)
    ac=st.number_input("(4,6)",1,9)
    ad=st.number_input("(5,6)",1,9)
    ae=st.number_input("(8,6)",1,9)
    af=st.number_input("(1,7)",1,9)
    ag=st.number_input("(2,7)",1,9)
    ah=st.number_input("(6,7)",1,9)
    ai=st.number_input("(9,7)",1,9)
    aj=st.number_input("(1,8)",1,9)
    ak=st.number_input("(2,8)",1,9)
    al=st.number_input("(3,8)",1,9)
    am=st.number_input("(6,8)",1,9)
    an=st.number_input("(8,8)",1,9)
    ao=st.number_input("(9,8)",1,9)
    ap=st.number_input("(1,9)",1,9)
    aq=st.number_input("(3,9)",1,9)
    ar=st.number_input("(4,9)",1,9)
    at=st.number_input("(6,9)",1,9)
    au=st.number_input("(7,9)",1,9)
    abc=st.number_input("Enter 1 for submitting.")
    if abc==1:
        if a==9 and b==4 and C==1 and c==3 and d==7 and e==7 and f==5 and g==6 and h==9 and i==4 and j==8 and k==6 and l==8 and m==5 and n==9 and o==9 and p==1 and q==4 and r==5 and s==7 and t==6 and u==1 and v==7 and w==3 and x==9 and y==8 and z==4 and aa==4 and ab==5 and ac==7 and ad==8 and ae==3 and af==9 and ag==7 and ah==4 and ai==5 and aj==5 and ak==1 and al==6 and am==8 and an==7 and ao==3 and ap==8 and aq==4 and ar==5 and at==7 and au==6:
            st.write("Correct!")
            st.balloons()
        else:
            st.write("Incorrect.... Hard luck!")
    
    
