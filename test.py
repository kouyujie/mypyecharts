#coding=utf-8
from __future__ import unicode_literals
from flask import Flask, render_template
import xlrd

app = Flask(__name__)  
 
@app.route('/')  
def app_0():  
    return "<h1>快修数据演示</h1>  <br> <a href='/one'>柱状图</a> <br> <a href='/two'>仪表盘</a>"

@app.route('/one')
def app_1():  
    from pyecharts import Bar
    i = 1
    xx = []
    yy = []

    xx1 = []
    yy1 = []
    bar = Bar("每日任务量", "快修组", width=1910, height=1060 )
    #bar.use_theme('dark')

    try:
        book = xlrd.open_workbook(u"快修-产量、效率、质量模板.xlsx")
        s = book.sheet_by_index(1)

        while i <= 20:
            #print s.cell_value( 3+i,0 ),s.cell_value( 3+i,1 )
            xx.append( s.cell_value( 3+i,0 ) )
            yy.append( s.cell_value( 3+i,1 ) )
            xx1.append( s.cell_value( 3+i,0 ) )
            yy1.append( s.cell_value( 3+i,4 ) )
            i += 1
    except IOError as err:
        print('File error:' + str(err))

    bar.add("审核量",xx,yy,mark_line=["average"], mark_point=["max", "min"],is_label_show = 1,label_pos = 'inside' , is_toolbox_show = False)
    bar.add("修改量",xx1,yy1,mark_line=["average"], mark_point=["max", "min"],is_label_show = 1,label_pos = 'inside', is_toolbox_show = False)

    ret_html = render_template('pyecharts.html',
                           myechart=bar.render_embed(),
                               mytitle=u"每日任务量数据",
                           host='/static',
                           script_list=bar.get_js_dependencies())
    return ret_html

@app.route('/two')  
def app_2():  
    from pyecharts import Gauge  
  
    gauge = Gauge("快修完成情况","任务数",width=800, height=400)  
    gauge.add("审核", "", 86.66,scale_range=[0,100],angle_range=[180,0])  
  
    gauge1 = Gauge("快修完成情况","任务数",width=800, height=400)  
    gauge1.add("修改", "", 88.99)  
    ret_html = render_template('pyecharts.html',  
                           myechart=gauge.render_embed()+gauge1.render_embed(),  
                               mytitle=u"快修数据演示",
                           host='/static',  
                           script_list=gauge.get_js_dependencies())  
    return ret_html  

if __name__ == '__main__':
  
    app.run(host='0.0.0.0',port=5018,debug=True)
