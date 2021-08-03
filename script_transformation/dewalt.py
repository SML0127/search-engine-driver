def user_defined_export(graph_mgr, node_id, node_properties):
    try:
        result = {}

        result['display'] = 'T'
        if node_properties['brand'] is None:
           node_properties['brand'] = 'DEWALT'
        result['product_name'] = node_properties['brand'] + ' - ' + node_properties['name']
        print("")
        print("product=["+str(result['product_name'])+"]");
        print("0.zipcode=["+str(node_properties['zipcode'])+"]");

        delivery_charge_list = [
            [0, 0.5, 10.2, 1223, 12475],
            [0.5, 1, 12.3, 1223, 15043],
            [1, 1.5, 14.5, 1223, 17734],
            [1.5, 2, 16.6, 1223, 20302],
            [2, 2.5, 18.7, 1223, 22870],
            [2.5, 3, 20.8, 1223, 25438],
            [3, 3.5, 23, 1223, 28129],
            [3.5, 4, 25.1, 1223, 30697],
            [4, 4.5, 27.2, 1223, 33266],
            [4.5, 5, 29.3, 1223, 35834],
            [5, 5.5, 31.5, 1223, 38525],
            [5.5, 6, 33.6, 1223, 41093],
            [6, 6.5, 35.7, 1223, 43661],
            [6.5, 7, 37.8, 1223, 46229],
            [7, 7.5, 40, 1223, 48920],
            [7.5, 8, 42.1, 1223, 51488],
            [8, 8.5, 44.2, 1223, 54057],
            [8.5, 9, 46.3, 1223, 56625],
            [9, 9.5, 48.5, 1223, 59316],
            [9.5, 10, 50.6, 1223, 61884],
            [10, 10.5, 52.7, 1223, 64452],
            [10.5, 11, 54.8, 1223, 67020],
            [11, 11.5, 57, 1223, 69711],
            [11.5, 12, 59.1, 1223, 72279],
            [12, 12.5, 61.2, 1223, 74848],
            [12.5, 13, 63.3, 1223, 77416],
            [13, 13.5, 65.5, 1223, 80107],
            [13.5, 14, 67.6, 1223, 82675],
            [14, 14.5, 69.7, 1223, 85243],
            [14.5, 15, 71.8, 1223, 87811],
            [15, 15.5, 74, 1223, 90502],
            [15.5, 16, 76.1, 1223, 93070],
            [16, 16.5, 78.2, 1223, 95639],
            [16.5, 17, 80.3, 1223, 98207],
            [17, 17.5, 82.5, 1223, 100898],
            [17.5, 18, 84.6, 1223, 103466],
            [18, 18.5, 86.7, 1223, 106034],
            [18.5, 19, 88.8, 1223, 108602],
            [19, 19.5, 91, 1223, 111293],
            [19.5, 20, 93.1, 1223, 113861],
            [20, 20.5, 95.2, 1223, 116430],
            [20.5, 21, 97.3, 1223, 118998],
            [21, 21.5, 99.5, 1223, 121689],
            [21.5, 22, 101.6, 1223, 124257],
            [22, 22.5, 103.7, 1223, 126825],
            [22.5, 23, 105.8, 1223, 129393],
            [23, 23.5, 108, 1223, 132084],
            [23.5, 24, 110.1, 1223, 134652],
            [24, 24.5, 112.2, 1223, 137221],
            [24.5, 25, 114.3, 1223, 139789],
            [25, 25.5, 116.5, 1223, 142480],
            [25.5, 26, 118.6, 1223, 145048],
            [26, 26.5, 120.7, 1223, 147616],
            [26.5, 27, 122.8, 1223, 150184],
            [27, 27.5, 125, 1223, 152875],
            [27.5, 28, 127.1, 1223, 155443],
            [28, 28.5, 129.2, 1223, 158012],
            [28.5, 29, 131.3, 1223, 160580],
            [29, 29.5, 133.5, 1223, 163271],
            [29.5, 30, 135.6, 1223, 165839],
            [30, 30.5, 147.9, 1223, 180882],
            [30.5, 31, 150, 1223, 183450],
            [31, 31.5, 152.2, 1223, 186141],
            [31.5, 32, 154.3, 1223, 188709],
            [32, 32.5, 156.4, 1223, 191277],
            [32.5, 33, 158.5, 1223, 193846],
            [33, 33.5, 160.7, 1223, 196536],
            [33.5, 34, 162.8, 1223, 199104],
            [34, 34.5, 164.9, 1223, 201673],
            [34.5, 35, 167, 1223, 204241],
            [35, 35.5, 169.2, 1223, 206932],
            [35.5, 36, 171.3, 1223, 209500],
            [36, 36.5, 173.4, 1223, 212068],
            [36.5, 37, 175.5, 1223, 214637],
            [37, 37.5, 177.7, 1223, 217327],
            [37.5, 38, 179.8, 1223, 219895],
            [38, 38.5, 181.9, 1223, 222464],
            [38.5, 39, 184, 1223, 225032],
            [39, 39.5, 186.2, 1223, 227723],
            [39.5, 40, 188.3, 1223, 230291],
            [40, 40.5, 190.4, 1223, 232859],
            [40.5, 41, 192.5, 1223, 235428],
            [41, 41.5, 194.7, 1223, 238118],
            [41.5, 42, 196.8, 1223, 240686],
            [42, 42.5, 198.9, 1223, 243255],
            [42.5, 43, 201, 1223, 245823],
            [43, 43.5, 203.2, 1223, 248514],
            [43.5, 44, 205.3, 1223, 251082],
            [44, 44.5, 207.4, 1223, 253650],
            [44.5, 45, 209.5, 1223, 256219],
            [45, 45.5, 211.7, 1223, 258909],
            [45.5, 46, 213.8, 1223, 261477],
            [46, 46.5, 215.9, 1223, 264046],
            [46.5, 47, 218, 1223, 266614],
            [47, 47.5, 220.2, 1223, 269305],
            [47.5, 48, 222.3, 1223, 271873],
            [48, 48.5, 224.4, 1223, 274441],
            [48.5, 49, 226.5, 1223, 277010],
            [49, 49.5, 228.7, 1223, 279700],
            [49.5, 50, 230.8, 1223, 282268],
            [50, 50.5, 258.4, 1223, 316023],
            [50.5, 51, 260.5, 1223, 318592],
            [51, 51.5, 262.7, 1223, 321282],
            [51.5, 52, 264.8, 1223, 323850],
            [52, 52.5, 266.9, 1223, 326419],
            [52.5, 53, 269, 1223, 328987],
            [53, 53.5, 271.2, 1223, 331678],
            [53.5, 54, 273.3, 1223, 334246],
            [54, 54.5, 275.4, 1223, 336814],
            [54.5, 55, 277.5, 1223, 339383],
            [55, 55.5, 279.7, 1223, 342073],
            [55.5, 56, 281.8, 1223, 344641],
            [56, 56.5, 283.9, 1223, 347210],
            [56.5, 57, 286, 1223, 349778],
            [57, 57.5, 288.2, 1223, 352469],
            [57.5, 58, 290.3, 1223, 355037],
            [58, 58.5, 292.4, 1223, 357605],
            [58.5, 59, 294.5, 1223, 360174],
            [59, 59.5, 296.7, 1223, 362864],
            [59.5, 60, 298.8, 1223, 365432],
            [60, 60.5, 300.9, 1223, 368001],
            [60.5, 61, 303, 1223, 370569],
            [61, 61.5, 305.2, 1223, 373260],
            [61.5, 62, 307.3, 1223, 375828],
            [62, 62.5, 309.4, 1223, 378396],
            [62.5, 63, 311.5, 1223, 380965],
            [63, 63.5, 313.7, 1223, 383655],
            [63.5, 64, 315.8, 1223, 386223],
            [64, 64.5, 317.9, 1223, 388792],
            [64.5, 65, 320, 1223, 391360],
            [65, 65.5, 322.2, 1223, 394051],
            [65.5, 66, 324.3, 1223, 396619],
            [66, 66.5, 326.4, 1223, 399187],
            [66.5, 67, 328.5, 1223, 401756],
            [67, 67.5, 330.7, 1223, 404446],
            [67.5, 68, 332.8, 1223, 407014],
            [68, 68.5, 334.9, 1223, 409583],
            [68.5, 69, 337, 1223, 412151],
            [69, 69.5, 339.2, 1223, 414842],
            [69.5, 70, 341.3, 1223, 417410],
            [70, 70.5, 343.4, 1223, 419978],
            [70.5, 71, 345.5, 1223, 422547],
            [71, 71.5, 347.7, 1223, 425237],
            [71.5, 72, 349.8, 1223, 427805],
            [72, 72.5, 351.9, 1223, 430374],
            [72.5, 73, 354, 1223, 432942],
            [73, 73.5, 356.2, 1223, 435633],
            [73.5, 74, 358.3, 1223, 438201],
            [74, 74.5, 360.4, 1223, 440769],
            [74.5, 75, 362.5, 1223, 443338],
            [75, 75.5, 364.7, 1223, 446028],
            [75.5, 76, 366.8, 1223, 448596],
            [76, 76.5, 368.9, 1223, 451165],
            [76.5, 77, 371, 1223, 453733],
            [77, 77.5, 373.2, 1223, 456424],
            [77.5, 78, 375.3, 1223, 458992],
            [78, 78.5, 377.4, 1223, 461560],
            [78.5, 79, 379.5, 1223, 464129],
            [79, 79.5, 381.7, 1223, 466819],
            [79.5, 80, 383.8, 1223, 469387],
            [80, 80.5, 385.9, 1223, 471956],
            [80.5, 81, 388, 1223, 474524],
            [81, 81.5, 390.2, 1223, 477215],
            [81.5, 82, 392.3, 1223, 479783],
            [82, 82.5, 394.4, 1223, 482351],
            [82.5, 83, 396.5, 1223, 484920],
            [83, 83.5, 398.7, 1223, 487610],
            [83.5, 84, 400.8, 1223, 490178],
            [84, 84.5, 402.9, 1223, 492747],
            [84.5, 85, 405, 1223, 495315],
            [85, 85.5, 407.2, 1223, 498006],
            [85.5, 86, 409.3, 1223, 500574],
            [86, 86.5, 411.4, 1223, 503142],
            [86.5, 87, 413.5, 1223, 505711],
            [87, 87.5, 415.7, 1223, 508401],
            [87.5, 88, 417.8, 1223, 510969],
            [88, 88.5, 419.9, 1223, 513538],
            [88.5, 89, 422, 1223, 516106],
            [89, 89.5, 424.2, 1223, 518797],
            [89.5, 90, 426.3, 1223, 521365],
            [90, 90.5, 428.4, 1223, 523933],
            [90.5, 91, 430.5, 1223, 526502],
            [91, 91.5, 432.7, 1223, 529192],
            [91.5, 92, 434.8, 1223, 531760],
            [92, 92.5, 436.9, 1223, 534329],
            [92.5, 93, 439, 1223, 536897],
            [93, 93.5, 441.2, 1223, 539588],
            [93.5, 94, 443.3, 1223, 542156],
            [94, 94.5, 445.4, 1223, 544724],
            [94.5, 95, 447.5, 1223, 547293],
            [95, 95.5, 449.7, 1223, 549983],
            [95.5, 96, 451.8, 1223, 552551],
            [96, 96.5, 453.9, 1223, 555120],
            [96.5, 97, 456, 1223, 557688],
            [97, 97.5, 458.2, 1223, 560379],
            [97.5, 98, 460.3, 1223, 562947],
            [98, 98.5, 462.4, 1223, 565515],
            [98.5, 99, 464.5, 1223, 568084],
            [99, 99.5, 466.7, 1223, 570774],
            [99.5, 100, 468.8, 1223, 573342]
        ]

        weight = node_properties['additional_info_dict'].get('Shipping Weight', '5kg').lower()
        r = re.compile(re.compile(r"\d+(\.\d*)?"))
        print("1. weight=["+str(weight)+"]")
        try:
            b = float(re.match(r, weight).group(0))
            if weight.find('kg'):
                weight = float(b)
            elif weight.find('g'):
                weight = float(b) * 0.001
            elif weight.find('pound'):
                weight = float(b) * 0.453592
            elif weight.found('ounce'):
                weight = float(b) * 0.0283495
        except:
            weight = 5.0

        delivery_charge = 35834.0

        for charge in delivery_charge_list:
            if weight > charge[0] and weight <= charge[1]:
                delivery_charge = charge[-1]
                break
        print("2. delivery_charge=["+str(delivery_charge)+"]")

        price = node_properties['price']
        print("3. price=["+str(price)+"]")
        if str(price) == 'None':
           print("3.1 new_seller_price =[" + str(node_properties['new_seller_price']) + "]")
           print("3.1 Price(new_seller_price) =[" + str(Price.fromstring(node_properties['new_seller_price']).amount_float) + "]")
           print("3.2 new_seller_shipping_price =[" + str(node_properties['new_seller_shipping_price']) + "]")
           print("3.2 Price(new_seller_shipping_price) =[" + str(Price.fromstring(node_properties['new_seller_shipping_price']).amount_float) + "]")
        else:
           shipping_price = node_properties['shipping_price']  
           print("3.3 shipping price=["+str(shipping_price)+"]");
           
        amount = 0.0
        if str(price) == 'None':
            amount = Price.fromstring(node_properties['new_seller_price']).amount_float;
            if str(node_properties['new_seller_shipping_price']) != 'None':
               amount = amount + Price.fromstring(node_properties['new_seller_shipping_price']).amount_float;
        else:
            amount = Price.fromstring(price).amount_float;
            if str(shipping_price) != 'None':
               amount = amount + Price.fromstring(shipping_price).amount_float;
               print("3.4 price,shipping,sum=["+str(price)+"]["+str(shipping_price)+"]["+str(amount)+"]");

        eur2usd = 1.1;
        dollar2krw = 1223;
        tariffRate = 0.08 if amount >= 200 else 0;
        taxRate = 0.1 if amount >= 200 else 0;
        margin_rate = 0.15;
        minimum_margin = 15000.0;
        lowest_price = -1;

        supplyPrice = dollar2krw * amount + delivery_charge
        margin = supplyPrice * margin_rate
        retailPriceWithoutMargin = ((supplyPrice) * (1 + tariffRate)) * (1 + taxRate)
        retailPrice = retailPriceWithoutMargin + margin
        buf = 5000
        isCompetitiveProduct = True

        if lowest_price == -1:
            adjRetailPrice = retailPrice
        else:
            adjRetailPrice = lowest_price - buf

        adjMargin = adjRetailPrice - retailPriceWithoutMargin
        true_min_margin = max(minimum_margin, (retailPriceWithoutMargin + adjMargin) * 0.065)
        if adjMargin < true_min_margin:
            adjMargin = true_min_margin
            isCompetitiveProduct = False
        price = retailPriceWithoutMargin + adjMargin

        result['price'] = str(price)
        print("4. supply_price = ["+ str(result['price'])+"]")
        result['supply_price'] = result['price']
        
        print("5. brand_code = [" + str(node_properties['brand']) + "]") 
        result['brand_code'] = node_properties['brand']
      
        result['detail_image'] = node_properties['images'][0]
        #print("6. OLD_Detail_Images=["+str(result['detail_image'][:10])+"]")
        if result['detail_image'] == '':
            if len(node_properties['images']) >= 2:
               result['detail_image'] = node_properties['images'][1]
        print("6. NEW_Detail_Images=["+str(result['detail_image'][:10])+"]")
        print("6.1 number of images=["+str(len(node_properties['images']))+"]")
        #print("6.2 images=["+str(node_properties['images'])+"]")

        result['additional_image'] = node_properties['images'][1:]
        result['selling'] = 'T'
        result['memo'] = node_properties.get('url', 'no url')
        print("7. url=["+str(result['memo'])+"]")

        #available_variant_ids = graph_mgr.find_n_hop_neighbors(node_id, [4])
        #print(available_variant_ids)
        variants = []
        variant = {}
        print("8. stock=["+ str(node_properties['stock']) +"]")
        if str(node_properties['stock']) == 'None':
             variant['stock'] = 1
        else:
             variant['stock'] = int(node_properties['stock'])
        variants.append(variant)
        variant['size'] = "one size"
        variants.append(variant)
        #for variant_id in available_variant_ids:
        #    variant = graph_mgr.get_node_properties(variant_id)
        #    stock = variant.get('stock')
        #    matches = re.findall('\d+', stock)
        #    variant['stock'] = 10 if len(matches) == 0 else int(matches[0])
        #    variants.append(variant)
        #unavailable_variant_ids = graph_mgr.find_n_hop_neighbors(node_id, [5])
        #print(unavailable_variant_ids)
        #for variant_id in unavailable_variant_ids:
        #    variant = graph_mgr.get_node_properties(variant_id)
        #    variant['stock'] = 0
        #    variants.append(variant)
        if len(variants) == 0:
            result['has_option'] = 'F'
        else:
            result['has_option'] = 'T'
            result['variants'] = variants
            result['option_names'] = ['size']
        print("9. custom_produce_code=["+str(node_properties['asin'])+"]")
        result['custom_product_code'] = node_properties['asin']
        result['add_category_no'] = [{"category_no": 106, "recommend": "F", "new": "T"}]
        description_title = '<div><h2 style="text-align: center;">{}</h2><br><br></div>'.format(result['product_name'])
        description_images = '<center>'
        for image in node_properties['images']:
            description_images += '<br><img src=\"{}\"></img>'.format(image)
        description_images = '<h2>Images</h2>' + description_images + '</center>'
        description_content = "<div style='padding-left: 1em;'><h2>Description</h2><br><br>i<b>ASIN:</b>{}<br><br>{}<br><br>{}</div>".format(result['custom_product_code'],node_properties['description'],description_images)
        #description_content = "<div style='padding-left: 1em;'><h2>Description</h2><br><br>{}<br><br>{}<br><br>{}<br><br>{}</div>".format(
        #    node_properties['MaterialAndCare'], node_properties['Details'], node_properties['SizeAndFit'],
        #    description_images)
        result['description'] = description_title + description_content
    except:
        print(result.keys())
        print(node_properties['url'])
        raise
    print(result.keys())
    return result

