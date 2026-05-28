from typing import Any

import requests

from bs4 import BeautifulSoup

import bs4


def get_info_magnit(url):
    headers = {
        'authority': 'magnit.ru',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.107',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'sec-fetch-site': 'none',
        'referer': 'https',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'mg_udi=45778daf-50b2-452f-8b0e-613e566ea16a; nmg_dt=; shopCode=992301; x_shop_type=ME; _ym_uid=1776516551887206089; _ym_d=1776516551; _ym_visorc=b; _ym_isad=1'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    text = str(soup.body).split("₽")[0][-50:][::-1]
    # print(text.split(">")[0][-50:][::-1])
    # print(soup.title.text)
    txt = text.split(">")[0][-50:][::-1]
    name = str(soup.title.text).split(" – ")[0]
    ls = dict()
    ls["shop"] = "Магнит"
    ls["product"] = name
    ls["price"] = text.split(">")[0][-50:][::-1].split("\u200a")[0]

    #
    return ls


def get_info_lenta(url):
    cookies = {
        'GrowthBook_user_id': 'fdf99ea2-b311-7e97-c3ff-75bb427460c7',
        'PassportRefreshToken': '',
        'PassportAccessToken': '',
        'PassportExpiresIn': '',
        'UserSessionId': 'e578272b-f819-9908-9829-c390121c1c99',
        'Utk_SessionToken': '01FA44FD85685B724BBC5E4D93362E1E',
        'iap.uid': 'f2e2bc5792b84e86805fac78a8c7ad40',
        'App_Cache_MissionAddressMode': '%7B%22t%22%3A%22pickup%22%2C%22ids%22%3Atrue%2C%22ma%22%3A%7B%22i%22%3A3149%2C%22a%22%3A%220124%22%2C%22t%22%3A%22%D0%A2%D0%9A124%22%2C%22af%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%207-%D1%8F%20%D0%9A%D0%BE%D0%B6%D1%83%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%2C%209%20(%D0%A2%D0%A0%D0%A6%20%D0%9C%D0%BE%D0%B7%D0%B0%D0%B8%D0%BA%D0%B0)%22%2C%22ri%22%3A1%2C%22mt%22%3A%22HM%22%2C%22s%22%3Afalse%7D%7D',
        'flocktory-uuid': 'c23b42bd-b510-4a3a-b22d-da4458c83842-5',
        'tmr_lvid': '35f569253036a15cf7e71521dbc75886',
        'tmr_lvidTS': '1777142063632',
        'adrcid': 'AV4RKMBCoarA8ah9OIqjerg',
        '_ym_uid': '1777142064325930018',
        '_ym_d': '1777142064',
        'agree_with_cookie': 'true',
        '_bge_ci': 'BA1.1.7794651279.1779214316',
        '_bge_uid2': '8141640746625702563',
        'GrowthBook_Cookie_Experiments': 'exp_newui_chips.test%2C%20exp_web_chips_online.test%2C%20exp_big_card.test%2C%20exp_without_a_doorbell.test_A%2C%20exp_new_navigation_web.test%2C%20exp_web_mobile_tabbar.test%2C%20exp_web_personal_promo_delivery_chips.test%2C%20exp_new_navigation_web_search.test%2C%20exp_new_navigation_web_actions.test%2C%20exp_leave_order_at_door.test%2C%20exp_leave_order_at_door_new.test%2C%20exp_new_counter_web.test',
        'GrowthBook_experiments': 'experiment_web_cl_new_csi_v2.0%2Cexperiment_web_aa_test_202601.0%2Cexperiment_web_aa_2026_01_v1.0%2Cexperiment_web_delivery_after_promocode_v2.1',
        'qrator_jsr': '1779804778.250.z139SvB0EzqecVgm-6dtkqb6aqdrme7ppb7ajdn8ag82h9aoj-00',
        'qrator_jsid': '1779804778.250.z139SvB0EzqecVgm-97nfop5k7a0m2du00f4mfjc1emb9kt34',
        'App_Cache_MPK': 'mp300-b1de0bac2c257f3257bf5ef2eea4ecbc',
        'App_Cache_CitySlug': 'moscow',
        'Utk_DvcGuid': '230f99b0-3bfd-eace-22ca-49ea8e347285',
        'Utk_MrkGrpTkn': 'F02ED18A6E346122335F21A8DB8A5A4A',
        'App_Cache_City': '%7B%22centerLat%22%3A%2255.75322%22%2C%22centerLng%22%3A%2237.622552%22%2C%22id%22%3A1%2C%22isDefault%22%3Atrue%2C%22mainDomain%22%3Afalse%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%9E%22%2C%22slug%22%3A%22moscow%22%7D',
        'User_Agent': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F148.0.0.0%20Safari%2F537.36',
        'Is_Search_Bot': 'false',
        'spses.d58d': '*',
        'acs_3': '%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1779891220505%2C%22sl%22%3A%7B%22224%22%3A1779804820505%2C%221228%22%3A1779804820505%7D%7D',
        '_ym_visorc': 'b',
        'adrdel': '1779804822283',
        '_ym_isad': '2',
        'domain_sid': '4vtd8s78bmtXLwu3dinrB%3A1779804826688',
        'tmr_detect': '0%7C1779804830515',
        'spid.d58d': '0d5a2eb8-df14-418e-ba33-e23583159a75.1777142065.10.1779804948.1779558990.df9b614f-86f3-45d8-b4dd-34144ef5803f.aba221ea-f4d4-4adc-bfc6-687ec5b365fe.2c101458-1b99-4a3d-ad69-7066fcee76e2.1779804820298.49',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'client': 'angular_web_0.0.2',
        'content-type': 'application/json',
        'deviceid': '230f99b0-3bfd-eace-22ca-49ea8e347285',
        'experiments': 'exp_recommendation_cms.true, exp_lentapay.test, exp_profile_bell.test, exp_cl_omni_authorization.test, exp_fullscreen.test, exp_onboarding_editing_order.test, exp_cl_omni_refusalprintreceipts.test, exp_cl_new_csi.control, exp_delivery_price_info.test, exp_interval_jump.test, exp_cardOne_promo_type.test, exp_birthday_coupon_skus.test, exp_qr_cnc.test, exp_where_place_cnc.test, exp_editing_cnc_onboarding.test, exp_editing_cnc.test, exp_pickup_in_delivery.test, exp_items_by_rating.test, exp_prices_per_quantum.test, exp_web_chips_online.test, exp_banner_sbp_checkout_step_3.control, exp_badge_sbp_checkout_step_3.test_B, exp_profile_stories.test, exp_aa_test_2025_04.control, exp_search_items_by_date.test_B, exp_without_a_doorbell.test_A, exp_edit_payment_type.test, exp_new_matrix.test, exp_progressbar_and_title.test, exp_promo_and_bonus.test, exp_new_navigation_web.test, exp_similar_goods_cart.test, exp_search_new_filters.test, exp_search_multicard.test, exp_fullscreen_inapp_vs_native.test1, exp_search_collections_ranking.test, exp_search_my_choice_stock_priority.test_b, exp_about_promocode.test_A, exp_personal_promo_detail_for_delivery.test_2, exp_web_personal_promo_delivery_chips.test, exp_ds_cnc_pers_recom.test, exp_search_pinned_reviews.test, exp_new_navigation_web_search.test, exp_new_navigation_web_actions.test, exp_status_assemble_completed.test, exp_online_subscription_discount.test, exp_search_no_stock.true, exp_leave_order_at_door.test, exp_leave_order_at_door_new.test, exp_search_quantity_discount_promo.test, exp_obi_webview.true, exp_huawei_adjust_new_tokens.true, exp_main_stories.test, exp_bubble_discount_startpage_mainpage.test, exp_ds_pers_recom_delivery_2.test, exp_search_ds_catboost_2.control, exp_novikov_test.OFF, exp_b2c_onboarding_send_cart.test, exp_b2c_send_cart.test, exp_web_aa_2026_01_v1.control, exp_web_cancel_to_edit_cnc.test, exp_ch_how_much_unit.test, exp_ds_cat_diversity.test, exp_test_toggle_b2b_b2c_web.test, exp_new_counter_web.test, exp_swap_empty_delivery_info.test_B, exp_swap_min_delivery_info.test_B, exp_authorization_vpn.test, exp_b2b_web_legal_entity_id_new.true, exp_delivery_after_promocode.test, exp_ch22405cartwithoutmonolith.test, exp_web_linking_sbp.efault, exp_non9.OFF',
        'origin': 'https://lenta.com',
        'priority': 'u=1, i',
        'referer': 'https://lenta.com/search/%D1%85%D0%BB%D0%B5%D0%B1/',
        'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sessiontoken': '01FA44FD85685B724BBC5E4D93362E1E',
        'traceparent': '00-6ba693e8c7f433bb83fd54b7b6000c5f-9b94edf4da1885d9-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        'x-delivery-mode': 'pickup',
        'x-device-brand': '',
        'x-device-id': '230f99b0-3bfd-eace-22ca-49ea8e347285',
        'x-device-name': '',
        'x-device-os': 'Web',
        'x-device-os-version': '12.4.8',
        'x-device-web-platform': 'desktop_web',
        'x-domain': 'moscow',
        'x-organization-id': '',
        'x-platform': 'omniweb',
        'x-retail-brand': 'lo',
        'x-span-id': '9b94edf4da1885d9',
        'x-trace-id': '6ba693e8c7f433bb83fd54b7b6000c5f',
        'x-user-session-id': 'e578272b-f819-9908-9829-c390121c1c99',
        # 'cookie': 'GrowthBook_user_id=fdf99ea2-b311-7e97-c3ff-75bb427460c7; PassportRefreshToken=; PassportAccessToken=; PassportExpiresIn=; UserSessionId=e578272b-f819-9908-9829-c390121c1c99; Utk_SessionToken=01FA44FD85685B724BBC5E4D93362E1E; iap.uid=f2e2bc5792b84e86805fac78a8c7ad40; App_Cache_MissionAddressMode=%7B%22t%22%3A%22pickup%22%2C%22ids%22%3Atrue%2C%22ma%22%3A%7B%22i%22%3A3149%2C%22a%22%3A%220124%22%2C%22t%22%3A%22%D0%A2%D0%9A124%22%2C%22af%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%207-%D1%8F%20%D0%9A%D0%BE%D0%B6%D1%83%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%2C%209%20(%D0%A2%D0%A0%D0%A6%20%D0%9C%D0%BE%D0%B7%D0%B0%D0%B8%D0%BA%D0%B0)%22%2C%22ri%22%3A1%2C%22mt%22%3A%22HM%22%2C%22s%22%3Afalse%7D%7D; flocktory-uuid=c23b42bd-b510-4a3a-b22d-da4458c83842-5; tmr_lvid=35f569253036a15cf7e71521dbc75886; tmr_lvidTS=1777142063632; adrcid=AV4RKMBCoarA8ah9OIqjerg; _ym_uid=1777142064325930018; _ym_d=1777142064; agree_with_cookie=true; _bge_ci=BA1.1.7794651279.1779214316; _bge_uid2=8141640746625702563; GrowthBook_Cookie_Experiments=exp_newui_chips.test%2C%20exp_web_chips_online.test%2C%20exp_big_card.test%2C%20exp_without_a_doorbell.test_A%2C%20exp_new_navigation_web.test%2C%20exp_web_mobile_tabbar.test%2C%20exp_web_personal_promo_delivery_chips.test%2C%20exp_new_navigation_web_search.test%2C%20exp_new_navigation_web_actions.test%2C%20exp_leave_order_at_door.test%2C%20exp_leave_order_at_door_new.test%2C%20exp_new_counter_web.test; GrowthBook_experiments=experiment_web_cl_new_csi_v2.0%2Cexperiment_web_aa_test_202601.0%2Cexperiment_web_aa_2026_01_v1.0%2Cexperiment_web_delivery_after_promocode_v2.1; qrator_jsr=1779804778.250.z139SvB0EzqecVgm-6dtkqb6aqdrme7ppb7ajdn8ag82h9aoj-00; qrator_jsid=1779804778.250.z139SvB0EzqecVgm-97nfop5k7a0m2du00f4mfjc1emb9kt34; App_Cache_MPK=mp300-b1de0bac2c257f3257bf5ef2eea4ecbc; App_Cache_CitySlug=moscow; Utk_DvcGuid=230f99b0-3bfd-eace-22ca-49ea8e347285; Utk_MrkGrpTkn=F02ED18A6E346122335F21A8DB8A5A4A; App_Cache_City=%7B%22centerLat%22%3A%2255.75322%22%2C%22centerLng%22%3A%2237.622552%22%2C%22id%22%3A1%2C%22isDefault%22%3Atrue%2C%22mainDomain%22%3Afalse%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%9E%22%2C%22slug%22%3A%22moscow%22%7D; User_Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F148.0.0.0%20Safari%2F537.36; Is_Search_Bot=false; spses.d58d=*; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1779891220505%2C%22sl%22%3A%7B%22224%22%3A1779804820505%2C%221228%22%3A1779804820505%7D%7D; _ym_visorc=b; adrdel=1779804822283; _ym_isad=2; domain_sid=4vtd8s78bmtXLwu3dinrB%3A1779804826688; tmr_detect=0%7C1779804830515; spid.d58d=0d5a2eb8-df14-418e-ba33-e23583159a75.1777142065.10.1779804948.1779558990.df9b614f-86f3-45d8-b4dd-34144ef5803f.aba221ea-f4d4-4adc-bfc6-687ec5b365fe.2c101458-1b99-4a3d-ad69-7066fcee76e2.1779804820298.49',
    }

    json_data = {
        'query': 'хлеб',
        'filters': {
            'checkbox': [],
            'multicheckbox': [],
            'range': [],
        },
        'sort': {
            'type': 'popular',
            'order': 'desc',
        },
        'limit': 40,
        'offset': 0,
    }

    response = requests.post('https://lenta.com/api-gateway/v1/catalog/items', cookies=cookies, headers=headers,
                             json=json_data)
    t = response.text.split(',"name":')[-1]
    text = t.split(",")[0]
    pr = response.text.split('"price":')[-1]
    price = pr.split(',')[0]
    ls = dict()
    ls["shop"] = "Лента"
    ls["product"] = text
    ls["price"] = price

    #
    return ls


def get_info_patyorka(url):
    cookies = {
        'spid': '1776538965928_c364545c03f5d240e70330cbb7b271ec_ktb16qobri0mdrd4',
        '_ym_uid': '1776538968737585761',
        '_ym_d': '1776538968',
        'spjs': '1779804793656_21b9f564_013526a2_b874e22b27e241e36e66efdbc7aa48b9_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',
        'spsc': '1779804793656_f1a7c2fcb59ce283ab5d57336f95b22e_0PP2fMHJOkse894VuAhD0By6qf3OnkzR8goaJ2rJvXwZ',
        'SRV': 'a2f50263-07d9-496b-aa10-a56d8f322d31',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://5ka.ru',
        'priority': 'u=1, i',
        'referer': 'https://5ka.ru/',
        'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        'x-app-version': '0.1.1.dev',
        'x-device-id': 'ce79cfe2-220f-4e00-920d-72dbead7f427',
        'x-platform': 'webapp',
        'x-tenant-id': 'TC5',
        # 'cookie': 'spid=1776538965928_c364545c03f5d240e70330cbb7b271ec_ktb16qobri0mdrd4; _ym_uid=1776538968737585761; _ym_d=1776538968; spjs=1779804793656_21b9f564_013526a2_b874e22b27e241e36e66efdbc7aa48b9_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; spsc=1779804793656_f1a7c2fcb59ce283ab5d57336f95b22e_0PP2fMHJOkse894VuAhD0By6qf3OnkzR8goaJ2rJvXwZ; SRV=a2f50263-07d9-496b-aa10-a56d8f322d31',
    }

    params = {
        'mode': 'delivery',
        'include_restrict': 'true',
        'q': 'хлеб',
        'limit': '12',
    }

    response = requests.get('https://5d.5ka.ru/api/catalog/v3/stores/35XY/search', params=params, cookies=cookies,
                            headers=headers)
    #print(response)
    te = response.text.split(',"name":')[1]
    text = te.split(',')[0]
    pr = te.split('"prices":{"regular":')[1]
    price = pr.split(",")[0]
    ls = dict()
    ls["shop"] = "Пятёрочка"
    ls["product"] = text
    ls["price"] = price
    return ls

# def fff(url):
#     cookies = {
#         'mg_udi': '4005c5a4-0d14-4e86-874d-ac3fdad8f75c',
#         'nmg_dt': '',
#         'x_shop_type': 'ME',
#         '_ym_uid': '1776537710143112713',
#         '_ym_d': '1776537710',
#         'oxxfgh': '8219b48f-e802-466b-87d5-66e2ccf6b4d7%230%237884000000%235000%231800000%2312840',
#         'uwyii': '2a42fc6c-2596-bc2b-af14-ed80b291dff8',
#         'nmg_sp': 'Y',
#         'mg_uac': '1',
#         'shopCode': '%22992301%22',
#         'tmr_lvid': '6f78a3c1e1cb800fbb78f4a6dcb68cbb',
#         'tmr_lvidTS': '1778929623484',
#         '_ym_isad': '2',
#         'domain_sid': 'nseMmFJjUQjKwjKEYK3iz%3A1779478191345',
#         '_ym_visorc': 'b',
#         '__zzatw-magnit-rux': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UtO2UiGkwSI0BVCXopFhU0cylMDxJfcT4mLixxIU4bTxcmSBBXayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfnIsVAsLWz5KcHosN1dhMA8WEU1HFT1WUk9DKGsbcVhXL3AkF0hSfjsWa25HZ0dXTBdfQjs4WEERdU05MzUwa34mYCs5YxEOIRRDVlBGaWcVG0BIGC9LbnowRGohX0daKEZcUXUXXVo/KBVZcUsfbnozP14LMQ80HA==2A1R9A==',
#         'tmr_detect': '0%7C1779540019553',
#         'gsscw-magnit-rux': 'q4fH4jzcBuxNAeed/6EYCTK9RYJZMZIo+ypOJjdAp7pkAfKmp2EekPDDnPj+JxDF0+zrp/oUCaqUERUeKDI/1LeYskLqthu9pNvQcn/VdFZEkZtVL+CLUc3i09DdbtmvXNZVk+yvuLTo+sFU7wbK9Sl9S1CLC80iC9i73R64LO2USTsHS1+cUCnnPW6zGgRXghifGxdf+uON88rzF6Fetbwh5xed8DUrMOun8dKYonQ5U4LlMVoiq0zuufogljCgQ5vZ',
#         'cfidsw-magnit-rux': 'rIoplafLzrBmbC6ZrvKCDcEzZGsdbg4KJMpMmTW2Nig2JA+p8/i3QHUiauy2TJ3SKkyrD+kdgPL9RccwA3Yb9f+DYyCdFbt/dlbY+nXSHZ4AQEuJZlQu0DZcKCRUL0DHg/zNttbwk3ILlAWj0jpDGw9E6yGdIJivGIxEj+k=',
#         'cfidsw-magnit-rux': 'rIoplafLzrBmbC6ZrvKCDcEzZGsdbg4KJMpMmTW2Nig2JA+p8/i3QHUiauy2TJ3SKkyrD+kdgPL9RccwA3Yb9f+DYyCdFbt/dlbY+nXSHZ4AQEuJZlQu0DZcKCRUL0DHg/zNttbwk3ILlAWj0jpDGw9E6yGdIJivGIxEj+k=',
#         'gsscw-magnit-rux': 'q4fH4jzcBuxNAeed/6EYCTK9RYJZMZIo+ypOJjdAp7pkAfKmp2EekPDDnPj+JxDF0+zrp/oUCaqUERUeKDI/1LeYskLqthu9pNvQcn/VdFZEkZtVL+CLUc3i09DdbtmvXNZVk+yvuLTo+sFU7wbK9Sl9S1CLC80iC9i73R64LO2USTsHS1+cUCnnPW6zGgRXghifGxdf+uON88rzF6Fetbwh5xed8DUrMOun8dKYonQ5U4LlMVoiq0zuufogljCgQ5vZ',
#         'uwyiert': '798377f9-973e-df63-e4e0-e69fbbdd5b06',
#         'fgsscw-magnit-rux': 'NuPH8c140e144466019fcf60b263e63872f64ec5',
#     }
#
#     headers = {
#         'accept': 'application/json',
#         'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#         'baggage': 'sentry-environment=production,sentry-public_key=7992e659d14bf5d8da08d2e6a0706d0a,sentry-trace_id=11d5bce28b7e45b19d9bda2ed202f421,sentry-sampled=false,sentry-sample_rand=0.744404511486226,sentry-sample_rate=0.05',
#         'content-type': 'application/json',
#         'origin': 'https://magnit.ru',
#         'priority': 'u=1, i',
#         'referer': 'https://magnit.ru/',
#         'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'sentry-trace': '11d5bce28b7e45b19d9bda2ed202f421-9892dcec54f84ea9-0',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
#         'x-app-version': '2026.5.22-17.54',
#         'x-client-name': 'magnit',
#         'x-device-id': '4005c5a4-0d14-4e86-874d-ac3fdad8f75c',
#         'x-device-platform': 'Web',
#         'x-device-tag': 'disabled',
#         'x-gib-fgsscw-magnit-rux': 'NuPH8c140e144466019fcf60b263e63872f64ec5',
#         'x-gib-gsscw-magnit-rux': 'q4fH4jzcBuxNAeed/6EYCTK9RYJZMZIo+ypOJjdAp7pkAfKmp2EekPDDnPj+JxDF0+zrp/oUCaqUERUeKDI/1LeYskLqthu9pNvQcn/VdFZEkZtVL+CLUc3i09DdbtmvXNZVk+yvuLTo+sFU7wbK9Sl9S1CLC80iC9i73R64LO2USTsHS1+cUCnnPW6zGgRXghifGxdf+uON88rzF6Fetbwh5xed8DUrMOun8dKYonQ5U4LlMVoiq0zuufogljCgQ5vZ',
#         'x-new-magnit': 'true',
#         'x-platform-version': 'Windows Chrome 148',
#         # 'cookie': 'mg_udi=4005c5a4-0d14-4e86-874d-ac3fdad8f75c; nmg_dt=; x_shop_type=ME; _ym_uid=1776537710143112713; _ym_d=1776537710; oxxfgh=8219b48f-e802-466b-87d5-66e2ccf6b4d7%230%237884000000%235000%231800000%2312840; uwyii=2a42fc6c-2596-bc2b-af14-ed80b291dff8; nmg_sp=Y; mg_uac=1; shopCode=%22992301%22; tmr_lvid=6f78a3c1e1cb800fbb78f4a6dcb68cbb; tmr_lvidTS=1778929623484; _ym_isad=2; domain_sid=nseMmFJjUQjKwjKEYK3iz%3A1779478191345; _ym_visorc=b; __zzatw-magnit-rux=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UtO2UiGkwSI0BVCXopFhU0cylMDxJfcT4mLixxIU4bTxcmSBBXayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfnIsVAsLWz5KcHosN1dhMA8WEU1HFT1WUk9DKGsbcVhXL3AkF0hSfjsWa25HZ0dXTBdfQjs4WEERdU05MzUwa34mYCs5YxEOIRRDVlBGaWcVG0BIGC9LbnowRGohX0daKEZcUXUXXVo/KBVZcUsfbnozP14LMQ80HA==2A1R9A==; tmr_detect=0%7C1779540019553; gsscw-magnit-rux=q4fH4jzcBuxNAeed/6EYCTK9RYJZMZIo+ypOJjdAp7pkAfKmp2EekPDDnPj+JxDF0+zrp/oUCaqUERUeKDI/1LeYskLqthu9pNvQcn/VdFZEkZtVL+CLUc3i09DdbtmvXNZVk+yvuLTo+sFU7wbK9Sl9S1CLC80iC9i73R64LO2USTsHS1+cUCnnPW6zGgRXghifGxdf+uON88rzF6Fetbwh5xed8DUrMOun8dKYonQ5U4LlMVoiq0zuufogljCgQ5vZ; cfidsw-magnit-rux=rIoplafLzrBmbC6ZrvKCDcEzZGsdbg4KJMpMmTW2Nig2JA+p8/i3QHUiauy2TJ3SKkyrD+kdgPL9RccwA3Yb9f+DYyCdFbt/dlbY+nXSHZ4AQEuJZlQu0DZcKCRUL0DHg/zNttbwk3ILlAWj0jpDGw9E6yGdIJivGIxEj+k=; cfidsw-magnit-rux=rIoplafLzrBmbC6ZrvKCDcEzZGsdbg4KJMpMmTW2Nig2JA+p8/i3QHUiauy2TJ3SKkyrD+kdgPL9RccwA3Yb9f+DYyCdFbt/dlbY+nXSHZ4AQEuJZlQu0DZcKCRUL0DHg/zNttbwk3ILlAWj0jpDGw9E6yGdIJivGIxEj+k=; gsscw-magnit-rux=q4fH4jzcBuxNAeed/6EYCTK9RYJZMZIo+ypOJjdAp7pkAfKmp2EekPDDnPj+JxDF0+zrp/oUCaqUERUeKDI/1LeYskLqthu9pNvQcn/VdFZEkZtVL+CLUc3i09DdbtmvXNZVk+yvuLTo+sFU7wbK9Sl9S1CLC80iC9i73R64LO2USTsHS1+cUCnnPW6zGgRXghifGxdf+uON88rzF6Fetbwh5xed8DUrMOun8dKYonQ5U4LlMVoiq0zuufogljCgQ5vZ; uwyiert=798377f9-973e-df63-e4e0-e69fbbdd5b06; fgsscw-magnit-rux=NuPH8c140e144466019fcf60b263e63872f64ec5',
#     }
#
#     json_data = {
#         'includeAdultGoods': True,
#         'pagination': {
#             'offset': 0,
#             'limit': 36,
#         },
#         'sort': {
#             'order': 'desc',
#             'type': 'popularity',
#         },
#         'term': 'сыр',
#         'storeCode': '992301',
#         'storeType': '6',
#         'catalogType': '1',
#     }
#
#     response = requests.post('https://magnit.ru/webgate/v2/goods/search', cookies=cookies, headers=headers,
#                              json=json_data)
#     te = response.text.split(',"name":')[1]
#     text = te.split(',')[0]
#     pr = te.split('')[1]
#
#     ls = dict()
#     ls["shop"] = "Пятёрочка"
#     ls["product"] = text
#     #ls["price"] = price
#     return response.text


if __name__ == '__main__':

        print(get_info_magnit("https://magnit.ru/product/1000026882-kubanskaya_burenka_moloko_past_2_5_0_93l_pl_but_vbd_6?shopCode=992301&shopType=6"))
        print(get_info_lenta("https://lenta.com/product/keks-yagodnoe-lukoshko-s-vishnejj-rossiya-270g-18236/"))
        print(get_info_patyorka("https://5ka.ru/product/khleb-sibirskiy-pekar-zernovoy-multizlakovyy-so-ln--4103219/"))
        #print(fff("https://magnit.ru/product/1000367086-belebeevskiy_syr_polutverdyy_belebeevskiy_45_190g_floupak_belebeevskiy_ordena_znak_pochyeta_molochny?shopCode=992301&shopType=6"))
