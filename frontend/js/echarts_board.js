function renderFeatureBoard(analysis) {
  if (typeof echarts === "undefined") {
    return;
  }

  let board = document.getElementById("featureBoard");
  if (!board) {
    board = document.createElement("div");
    board.id = "featureBoard";
    board.style.width = "100%";
    board.style.height = "220px";
    document.querySelector(".panel").appendChild(board);
  }

  const chart = echarts.init(board);
  chart.setOption({
    backgroundColor: "transparent",
    radar: {
      indicator: [
        { name: "力度", max: 100 },
        { name: "活跃度", max: 100 },
        { name: "抒情性", max: 100 },
        { name: "复杂度", max: 100 },
        { name: "沉浸感", max: 100 }
      ]
    },
    series: [
      {
        type: "radar",
        data: [
          {
            value: analysis.feature_profile,
            areaStyle: {
              color: "rgba(175, 94, 44, 0.28)"
            },
            lineStyle: {
              color: "#af5e2c"
            }
          }
        ]
      }
    ]
  });
}
