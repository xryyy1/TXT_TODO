window.onload = function() {
    // 初始化ECharts实例
    var chart = echarts.init(document.getElementById('chart'));

    // 准备数据
    var titles = videoData.map(video => video['标题']);
    var viewCounts = videoData.map(video => video['观看量']);
    var danmakuCounts = videoData.map(video => video['弹幕数']);
    var likeCounts = videoData.map(video => video['点赞数']);

    // 配置图表
    var option = {
        title: {
            text: 'Bilibili 视频数据',
            subtext: '观看量、弹幕数、点赞数',
            left: 'center'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['观看量', '弹幕数', '点赞数'],
            left: 'left'
        },
        xAxis: {
            type: 'category',
            data: titles,
            axisLabel: {
                rotate: 45,
                interval: 0
            }
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name: '观看量',
                type: 'bar',
                data: viewCounts
            },
            {
                name: '弹幕数',
                type: 'bar',
                data: danmakuCounts
            },
            {
                name: '点赞数',
                type: 'bar',
                data: likeCounts
            }
        ]
    };

    // 使用配置项显示图表
    chart.setOption(option);
};
