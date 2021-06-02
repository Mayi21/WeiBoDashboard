var chart1Data;
var chart2Data;
var chart3XData;
var chart3Data;
var chart4Data;
var chart4LegendData;


function SetChart(){
    var mychart1 = echarts.init(document.getElementById('pie'), 'macarons');
    var option1 = {
        title : {
            text: '微博用户性别比例',
            subtext: '仅部分微博数据',
            x:'left'
        },
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient : 'vertical',
            x : 'center',
            // data:['男生比例','女生比例']
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                magicType : {
                    show: true,
                    type: ['pie', 'funnel'],
                    option: {
                        funnel: {
                            x: '25%',
                            width: '50%',
                            funnelAlign: 'left',
                            max: 3000
                        }
                    }
                },
            }
        },
        calculable : true,
        series : [{
                name:'性别比例',
                type:'pie',
                radius : '55%',
                center: ['50%', '60%'],
                label:{
                    textStyle:{
                        fontWeight: 300,
                        fontSize:15,
                    }
                },
                data: chart1Data,
            }
        ]
    };
    mychart1.setOption(option1);
    var mychart2 = echarts.init(document.getElementById('map'), 'macarons');
    var option2 = {
        title : {
            text: '微博人口分布',
            subtext: '仅部分微博数据',
        },
        tooltip : {
            trigger: 'item'
        },
        dataRange: {
            orient: 'horizontal',
            min: 0,
            max: 800,
            text:['高','低'],           // 文本，默认为数值文本
            splitNumber:0
        },
        toolbox: {
            show : true,
            orient: 'vertical',
            x:'right',
            y:'center',
            feature : {
                mark : {show: true},
            }
        },
        series : [
            {
                name: '微博人口分布',
                type: 'map',
                mapType: 'china',
                mapLocation: {
                    x: 'left'
                },
                selectedMode : 'multiple',
                itemStyle:{
                    normal:{label:{show:true}},
                    emphasis:{label:{show:true}}
                },
                data: chart2Data,
            },
        ],
        animation: true
    };
    mychart2.setOption(option2);
    var mychart3 = echarts.init(document.getElementById('ployChart'), 'macarons');
    var option3 = {
        title: {
          text: '微博发送时间',
          subtext: '仅部分微\n博数据',
        },
        tooltip : {
            trigger: 'axis'
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                magicType : {show: true, type: ['line', 'bar']},
            }
        },
        calculable : true,
        dataZoom : {
            show : true,
            realtime : true,
            start : 20,
            end : 80
        },
        xAxis : [
            {
                name: '数量',
                type: 'category',
                boundaryGap: false,
                data: chart3XData,
            }
        ],
        yAxis : [
            {
                name: '日期',
                type : 'value'
            }
        ],
        series : [
            {
                name: '发博数',
                type:'line',
                data: chart3Data,
            }
        ]
    };
    mychart3.setOption(option3)
    var mychart4 = echarts.init(document.getElementById('phonePie'), 'macarons');
    var option4 = {
        title : {
            text: '微博来源',
            subtext: '仅部分微博数据',
            x:'left'
        },
        tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            x : 'center',
            y : 'bottom',
            data: chart4LegendData,
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                magicType : {
                    show: true,
                    type: ['pie', 'funnel']
                },
            }
        },
        calculable : true,
        series : [
            {
                name:'数量',
                type:'pie',
                radius : '45%',
                center : ['50%', '50%'],
                roseType : 'area',
                x: 'center',               // for funnel
                max: 40,                // for funnel
                sort : 'ascending',     // for funnel
                data: chart4Data,
            }
        ]
    };
    mychart4.setOption(option4)
}
function GetData(){
    $.ajax({
        url: '/getsexratio/',
        type: 'POST',
        async: true,
        dataType: 'JSON',
        success: function (d){
            chart1Data = d;
            console.log(d)
        }
    })
    $.ajax({
        url: '/getmap/',
        type: 'POST',
        dataType: 'JSON',
        async: true,
        success: function (d){
            chart2Data = d;
            // console.log(chart2Data)
        }
    })
    // $.ajax({
    //     url: '/getsenddate/',
    //     type: 'POST',
    //     async: true,
    //     success: function (d){
    //         chart3XData = d[0];
    //         chart3Data = d[1];
    //     }
    // })
    // $.ajax({
    //     url: '/getweibosource/',
    //     type: 'POST',
    //     async: true,
    //     success: function (d){
    //         chart4LegendData = d[0];
    //         chart4Data = d[1];
    //     }
    // })
    $.ajax({
        url: '/getdatainfo/',
        type: 'POST',
        async: true,
        dataType: 'JSON',
        success: function (d){
            $('#upnum').append(d[0])
            $('#weibonum').append(d[1])
        }
    })
}
GetData();
SetChart();