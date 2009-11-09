// 省份按拼音首字母升序排列
PROVINCES = {
	'100':'北京市',
	'200':'广东省',
	'210':'上海市',
	'220':'天津市',
	'230':'重庆市',
	'240':'辽宁省',
	'250':'江苏省',
	'270':'湖北省',
	'280':'四川省',
	'290':'陕西省',
	'311':'河北省',
	'351':'山西省',
	'371':'河南省',
	'431':'吉林省',
	'451':'黑龙江省',
	'471':'内蒙古自治区',
	'531':'山东省',
	'551':'安徽省',
	'571':'浙江省',
	'591':'福建省',
	'731':'湖南省',
	'771':'广西壮族自治区',
	'791':'江西省',
	'851':'贵州省',
	'871':'云南省',
	'891':'西藏自治区',
	'898':'海南省',
	'931':'甘肃省',
	'951':'宁夏回族自治区',
	'971':'青海省',
	'991':'新疆维吾尔自治区',
}

CITIES = {
	'100':'北京',
	'200':'广州',
	'210':'上海',
	'220':'天津',
	'230':'重庆',
	'240':'沈阳',
	'250':'南京',
	'270':'武汉',
	'280':'成都',
	'290':'西安',
	'310':'邯郸',
	'311':'石家庄',
	'312':'保定',
	'313':'张家口',
	'314':'承德',
	'315':'唐山',
	'316':'廊坊',
	'317':'沧州',
	'318':'衡水',
	'319':'邢台',
	'335':'秦皇岛',
	'349':'朔州',
	'350':'忻州',
	'351':'太原',
	'352':'大同',
	'353':'阳泉',
	'354':'晋中',
	'355':'长治',
	'356':'晋城',
	'357':'临汾',
	'358':'吕梁',
	'359':'运城',
	'370':'商丘',
	'371':'郑州',
	'372':'安阳',
	'373':'新乡',
	'374':'许昌',
	'375':'平顶山',
	'376':'信阳',
	'377':'南阳',
	'378':'开封',
	'379':'洛阳',
	'391':'焦作',
	'392':'鹤壁',
	'393':'濮阳',
	'394':'周口',
	'395':'漯河',
	'396':'驻马店',
	'398':'三门峡',
	'410':'铁岭',
	'411':'大连',
	'412':'鞍山',
	'413':'抚顺',
	'414':'本溪',
	'415':'丹东',
	'416':'锦州',
	'417':'营口',
	'418':'阜新',
	'419':'辽阳',
	'421':'朝阳',
	'427':'盘锦',
	'429':'葫芦岛',
	'431':'长春',
	'432':'吉林',
	'433':'延边',
	'434':'四平',
	'435':'通化',
	'436':'白城',
	'437':'辽源',
	'438':'松原',
	'439':'白山',
	'451':'哈尔滨',
	'452':'齐齐哈尔',
	'453':'牡丹江',
	'454':'佳木斯',
	'455':'绥化',
	'456':'黑河',
	'457':'大兴安岭',
	'458':'伊春',
	'459':'大庆',
	'464':'七台河',
	'467':'鸡西',
	'468':'鹤岗',
	'469':'双鸭山',
	'470':'呼伦贝尔',
	'471':'呼和浩特',
	'472':'包头',
	'473':'乌海',
	'474':'乌兰察布',
	'475':'通辽',
	'476':'赤峰',
	'477':'鄂尔多斯',
	'478':'巴彦淖尔',
	'479':'锡林郭勒',
	'482':'兴安盟',
	'483':'阿拉善',
	'510':'无锡',
	'511':'镇江',
	'512':'苏州',
	'513':'南通',
	'514':'扬州',
	'515':'盐城',
	'516':'徐州',
	'517':'淮安',
	'518':'连云港',
	'519':'常州',
	'523':'泰州',
	'527':'宿迁',
	'530':'菏泽',
	'531':'济南',
	'532':'青岛',
	'533':'淄博',
	'534':'德州',
	'535':'烟台',
	'536':'潍坊',
	'537':'济宁',
	'538':'泰安',
	'539':'临沂',
	'543':'滨州',
	'546':'东营',
	'550':'滁州',
	'551':'合肥',
	'552':'蚌埠',
	'553':'芜湖',
	'554':'淮南',
	'555':'马鞍山',
	'556':'安庆',
	'557':'宿州',
	'558':'阜阳',
	'559':'黄山',
	'561':'淮北',
	'562':'铜陵',
	'563':'宣城',
	'564':'六安',
	'565':'巢湖',
	'566':'池州',
	'567':'亳州',
	'570':'衢州',
	'571':'杭州',
	'572':'湖州',
	'573':'嘉兴',
	'574':'宁波',
	'575':'绍兴',
	'576':'台州',
	'577':'温州',
	'578':'丽水',
	'579':'金华',
	'580':'舟山',
	'591':'福州',
	'592':'厦门',
	'593':'宁德',
	'594':'莆田',
	'595':'泉州',
	'596':'漳州',
	'597':'龙岩',
	'598':'三明',
	'599':'南平',
	'631':'威海',
	'632':'枣庄',
	'633':'日照',
	'634':'莱芜',
	'635':'聊城',
	'660':'汕尾',
	'662':'阳江',
	'663':'揭阳',
	'668':'茂名',
	'691':'西双版纳',
	'692':'德宏',
	'701':'鹰潭',
	'710':'襄樊',
	'711':'鄂州',
	'712':'孝感',
	'713':'黄冈',
	'714':'黄石',
	'715':'咸宁',
	'716':'荆州',
	'717':'宜昌',
	'718':'恩施',
	'719':'十堰',
	'722':'随州',
	'724':'荆门',
	'728':'江汉',
	'730':'岳阳',
	'731':'长沙',
	'732':'湘潭',
	'733':'株洲',
	'734':'衡阳',
	'735':'郴州',
	'736':'常德',
	'737':'益阳',
	'738':'娄底',
	'739':'邵阳',
	'743':'湘西',
	'744':'张家界',
	'745':'怀化',
	'746':'永州',
	'750':'江门',
	'751':'韶关',
	'752':'惠州',
	'753':'梅州',
	'754':'汕头',
	'755':'深圳',
	'756':'珠海',
	'757':'佛山',
	'758':'肇庆',
	'759':'湛江',
	'760':'中山',
	'762':'河源',
	'763':'清远',
	'766':'云浮',
	'768':'潮州',
	'769':'东莞',
	'770':'防城港',
	'771':'南宁',
	'772':'柳州',
	'773':'桂林',
	'774':'梧州',
	'775':'玉林',
	'776':'百色',
	'777':'钦州',
	'778':'河池',
	'779':'北海',
	'790':'新余',
	'791':'南昌',
	'792':'九江',
	'793':'上饶',
	'794':'抚州',
	'795':'宜春',
	'796':'吉安',
	'797':'赣州',
	'798':'景德镇',
	'799':'萍乡',
	'811':'眉山',
	'812':'攀枝花',
	'813':'自贡',
	'816':'绵阳',
	'817':'南充',
	'818':'达州',
	'819':'资阳',
	'825':'遂宁',
	'826':'广安',
	'827':'巴中',
	'830':'泸州',
	'831':'宜宾',
	'832':'内江',
	'833':'乐山',
	'834':'凉山',
	'835':'雅安',
	'836':'甘孜',
	'837':'阿坝',
	'838':'德阳',
	'839':'广元',
	'851':'贵阳',
	'852':'遵义',
	'853':'安顺',
	'854':'黔南',
	'855':'黔东南',
	'856':'铜仁',
	'857':'毕节',
	'858':'六盘水',
	'859':'黔西南',
	'870':'昭通',
	'871':'昆明',
	'872':'大理',
	'873':'红河',
	'874':'曲靖',
	'875':'保山',
	'876':'文山',
	'877':'玉溪',
	'878':'楚雄',
	'879':'普洱',
	'883':'临沧',
	'886':'怒江',
	'887':'迪庆',
	'888':'丽江',
	'891':'拉萨',
	'892':'日喀则',
	'893':'山南',
	'894':'林芝',
	'895':'昌都',
	'896':'那曲',
	'897':'阿里',
	'898':'海口',
	'901':'塔城',
	'902':'哈密',
	'903':'和田',
	'906':'阿勒泰',
	'908':'克孜勒苏',
	'909':'博尔塔拉',
	'910':'咸阳',
	'911':'延安',
	'912':'榆林',
	'913':'渭南',
	'914':'商洛',
	'915':'安康',
	'916':'汉中',
	'917':'宝鸡',
	'919':'铜川',
	'930':'临夏',
	'931':'兰州',
	'932':'定西',
	'933':'平凉',
	'934':'庆阳',
	'935':'武威',
	'936':'张掖',
	'937':'酒泉',
	'938':'天水',
	'939':'陇南',
	'941':'甘南',
	'943':'白银',
	'945':'金昌',
	'947':'嘉峪关',
	'951':'银川',
	'952':'石嘴山',
	'953':'吴忠',
	'954':'固原',
	'955':'中卫',
	'970':'海北',
	'971':'西宁',
	'972':'海东',
	'973':'黄南',
	'974':'海南州',
	'975':'果洛',
	'976':'玉树',
	'977':'海西',
	'979':'格尔木',
	'990':'克拉玛依',
	'991':'乌鲁木齐',
	'992':'奎屯',
	'993':'石河子',
	'994':'昌吉',
	'995':'吐鲁番',
	'996':'巴音郭楞',
	'997':'阿克苏',
	'998':'喀什',
	'999':'伊犁',
}

PROVINCE_CITY = {
	'100': [100],
	'210': [210],
	'898': [898],
	'871': [883,888,875,872,692,886,876,871,870,879,874,878,877,873,691,887,],
	'471': [474,473,482,472,470,471,478,476,475,477,479,483],
	'431': [432,434,433,438,436,439,437,435,431],
	'280': [833,832,834,817,831,827,839,826,838,280,812,830,836,811,816,813,819,818,825,837,835],
	'220': [220],
	'951': [955,953,954,952,951],
	'551': [567,564,551,556,563,557,565,566,561,554,550,553,552,562,558,555,559],
	'531': [546,539,631,534,633,632,538,531,537,533,543,536,535,635,634,530,532],
	'351': [357,358,352,351,350,354,356,349,359,355,353],
	'200': [769,760,766,757,200,752,663,753,754,660,750,762,755,763,759,768,756,758,668,662,751],
	'771': [779,771,772,773,774,778,775,776,777,770],
	'991': [991,999,908,990,909,995,903,902,998,901,992,996,994,993,997,906],
	'250': [250,513,527,519,516,514,510,523,517,515,512,518,511],
	'791': [793,792,791,796,795,794,790,798,799,797,701],
	'311': [312,315,316,313,314,317,311,335,318,319,310],
	'371': [398,376,377,394,370,372,375,378,373,379,395,393,391,374,371,396,392],
	'571': [578,576,573,574,571,577,572,575,580,570,579],
	'270': [719,715,712,717,718,270,728,716,724,710,711,722,713,714],
	'731': [738,730,736,744,745,733,746,732,743,737,734,739,735,731],
	'931': [930,931,947,938,932,933,934,936,935,941,943,937,945,939],
	'591': [598,599,592,593,595,596,591,594,597],
	'891': [893,891,892,895,894,896,897],
	'851': [858,853,857,851,852,856,855,854,859],
	'240': [415,411,413,421,414,240,427,417,429,419,410,416,418,412],
	'230': [230],
	'290': [910,914,915,917,911,912,916,913,290,919],
	'971': [975,979,972,970,974,977,976,971,973],
	'451': [464,458,454,469,451,457,459,453,455,467,468,456,452]
}

for (i in PROVINCE_CITY) {
	PROVINCE_CITY[i].sort();
}

var Province = new function() {
	
	/**
	 * 从省中文名反查 ID
	 */
	this.getIDByName = function(name) {
		for (i in PROVINCES) {
			if (PROVINCES[i] == name)
				return i;
		}
	}
	
	/**
	 * 从 ID 查中文名
	 */
	this.getNameByID = function(id) {
		return PROVINCES[id];
	}
	
	/**
	 * 根据省 ID 查下属的城市
	 */
	this.getCitiesByID = function(id) {
		var rel = PROVINCE_CITY[id];
		var tmp = {};
		
		if (rel) {
			for (var i = 0; i < rel.length; i++) {
				tmp[rel[i]] = CITIES[rel[i]];
			}
		}
		
		return tmp;
	}
	
}

var City = new function () {
	
	/**
	 * 从城市名反查 ID
	 */
	this.getIDByName = function(name) {
		for (i in CITIES) {
			if (CITIES[i] == name)
				return i;
		}
	}
	
	/**
	 * 从 ID 反查城市名
	 */
	this.getNameByID = function(id) {
		return CITIES[id];
	}
	
	/**
	 * 从城市反查省
	 */
	this.getProvinceByName = function(name) {
		for (i in CITIES) {
			if (CITIES[i] == name) {
				var pid = i.substring(0, 2) + '000000';
				return {'id': pid, 'name': PROVINCES[pid]};
			}
		}
	}
	
}