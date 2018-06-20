# coding=UTF-8  
#  flask echart  实验  
from flask import Flask, render_template  
app = Flask(__name__)  
 
@app.route('/')  
def app_0():  
    return "<h1>EChart数据演示</h1>  <br> <a href='/one'>柱状图</a> <br> <a href='/two'>仪表盘</a>"  
 
@app.route('/one')  
def app_1():  
    from pyecharts import Bar  
  
    bar = Bar("一周任务量", "快修组",width=1920,height=1080,background_color='#000')  
    bar.add("审核量", ["周一", "周二", "周三", "周四", "周五", "周六","周日"], [5, 20, 36, 10, 75, 90,28])  
    bar.add("修改量", ["周一", "周二", "周三", "周四", "周五", "周六","周日"], [25, 10, 56, 70, 25, 40,88])  
    ret_html = render_template('pyecharts.html',  
                           myechart=bar.render_embed(),  
                               mytitle=u"数据演示",  
                           host='/static',  
                           script_list=bar.get_js_dependencies())  
    return ret_html  
 
@app.route('/two')  
def app_2():  
    from pyecharts import Gauge  
  
    gauge = Gauge("快修完成情况","任务数",width=600, height=300)  
    gauge.add("审核", "", 86.66,scale_range=[0,100],angle_range=[180,0])  
  
    gauge1 = Gauge("快修完成情况","任务数",width=600, height=300)  
    gauge1.add("修改", "", 88.99)  
    ret_html = render_template('pyecharts.html',  
                           myechart=gauge.render_embed()+gauge1.render_embed(),  
                               mytitle=u"数据演示",  
                           host='/static',  
                           script_list=gauge.get_js_dependencies())  
    return ret_html  
  
if __name__ == '__main__':  
  
    app.run(host='0.0.0.0',port=5018)  
