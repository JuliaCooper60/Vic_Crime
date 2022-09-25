

var bardata;
// Create a lsit of LGAs
var lgalist = 
['All',
 'Alpine',
 'Ararat',
 'Ballarat',
 'Banyule',
 'Bass Coast',
 'Baw Baw',
 'Bayside',
 'Benalla',
 'Boroondara',
 'Brimbank',
 'Buloke',
 'Campaspe',
 'Cardinia',
 'Casey',
 'Central Goldfields',
 'Colac-Otway',
 'Corangamite',
 'Darebin',
 'East Gippsland',
 'Frankston',
 'Gannawarra',
 'Glen Eira',
 'Glenelg',
 'Golden Plains',
 'Greater Bendigo',
 'Greater Dandenong',
 'Greater Geelong',
 'Greater Shepparton',
 'Hepburn',
 'Hindmarsh',
 'Hobsons Bay',
 'Horsham',
 'Hume',
 'Indigo',
 'Kingston',
 'Knox',
 'Latrobe',
 'Loddon',
 'Macedon Ranges',
 'Manningham',
 'Mansfield',
 'Maribyrnong',
 'Maroondah',
 'Melbourne',
 'Melton',
 'Mildura',
 'Mitchell',
 'Moira',
 'Monash',
 'Moonee Valley',
 'Moorabool',
 'Moreland',
 'Mornington Peninsula',
 'Mount Alexander',
 'Moyne',
 'Murrindindi',
 'Nillumbik',
 'Northern Grampians',
 'Port Phillip',
 'Pyrenees',
 'Queenscliffe',
 'South Gippsland',
 'Southern Grampians',
 'Stonnington',
 'Strathbogie',
 'Surf Coast',
 'Swan Hill',
 'Towong',
 'Wangaratta',
 'Warrnambool',
 'Wellington',
 'West Wimmera',
 'Whitehorse',
 'Whittlesea',
 'Wodonga',
 'Wyndham',
 'Yarra',
 'Yarra Ranges',
 'Yarriambiack']

 d3.json('api/crime_summary').then((barData) => {

  barDataFull = barData;
  bardata = barData.All;
  var ctx = document.getElementById('myChart').getContext('2d');
  var lgaselect = document.getElementById('selLGA');
  myChart = new Chart(ctx, 
    {
  data: bardata,
  type: 'bar',
  responsive:true,
  scales: {
    x:{
      stacked:true
  },
    y:{
      stacked:true
    },

  }

  });


for (i=0; i< lgalist.length; i++)
{
var opt = document.createElement("option");
  opt.text = lgalist[i];
  lgaselect.add(opt); 
}

lgaselect.selectedIndex = 0;

  });


function optionChanged(sValue)
{
	bardata = barDataFull[sValue];
	myChart.data = bardata;
	myChart.update();
}


