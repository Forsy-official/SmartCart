
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
    #print(text.split(">")[0][-50:][::-1])
    #print(soup.title.text)
    txt = text.split(">")[0][-50:][::-1]
    name = str(soup.title.text).split(" – ")[0]
    ls = dict()
    ls["shop"] = "Магнит"
    ls["product"] = name
    ls["price"] = text.split(">")[0][-50:][::-1].split("\u200a")[0]

    #
    return ls

def get_info_lenta(url):
    import requests

    cookies = {
        'User_Agent': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F148.0.0.0%20Safari%2F537.36',
        'Is_Search_Bot': 'false',
        'agree_with_cookie': 'true',
        'GrowthBook_user_id': 'fdf99ea2-b311-7e97-c3ff-75bb427460c7',
        'App_Cache_MPK': 'mp300-b1de0bac2c257f3257bf5ef2eea4ecbc',
        'App_Cache_CitySlug': 'moscow',
        'PassportRefreshToken': '',
        'PassportAccessToken': '',
        'PassportExpiresIn': '',
        'UserSessionId': 'e578272b-f819-9908-9829-c390121c1c99',
        'Utk_SessionToken': '01FA44FD85685B724BBC5E4D93362E1E',
        'iap.uid': 'f2e2bc5792b84e86805fac78a8c7ad40',
        'App_Cache_City': '%7B%22centerLat%22%3A%2255.75322%22%2C%22centerLng%22%3A%2237.622552%22%2C%22id%22%3A1%2C%22isDefault%22%3Atrue%2C%22mainDomain%22%3Afalse%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%9E%22%2C%22slug%22%3A%22moscow%22%7D',
        'App_Cache_MissionAddressMode': '%7B%22t%22%3A%22pickup%22%2C%22ids%22%3Atrue%2C%22ma%22%3A%7B%22i%22%3A3149%2C%22a%22%3A%220124%22%2C%22t%22%3A%22%D0%A2%D0%9A124%22%2C%22af%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%207-%D1%8F%20%D0%9A%D0%BE%D0%B6%D1%83%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%2C%209%20(%D0%A2%D0%A0%D0%A6%20%D0%9C%D0%BE%D0%B7%D0%B0%D0%B8%D0%BA%D0%B0)%22%2C%22ri%22%3A1%2C%22mt%22%3A%22HM%22%2C%22s%22%3Afalse%7D%7D',
        'flocktory-uuid': 'c23b42bd-b510-4a3a-b22d-da4458c83842-5',
        'tmr_lvid': '35f569253036a15cf7e71521dbc75886',
        'tmr_lvidTS': '1777142063632',
        'adrcid': 'AV4RKMBCoarA8ah9OIqjerg',
        '_ym_uid': '1777142064325930018',
        '_ym_d': '1777142064',
        'agree_with_cookie': 'true',
        'Utk_DvcGuid': '964a9f25-271c-2aba-c33a-bd5100ac01db',
        'Utk_MrkGrpTkn': '3B3669E90394E50F2924CB14536D461F',
        'User_Agent': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F148.0.0.0%20Safari%2F537.36',
        'Is_Search_Bot': 'false',
        '_ym_isad': '1',
        'spses.d58d': '*',
        'domain_sid': '4vtd8s78bmtXLwu3dinrB%3A1778929028631',
        'acs_3': '%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1779016279847%2C%22sl%22%3A%7B%22224%22%3A1778929879847%2C%221228%22%3A1778929879847%7D%7D',
        'adrdel': '1778929881370',
        'qrator_jsid': '1778928978.107.Lia7wHZqzD2xhuUl-44j4dv4ehempdjfidmu2a1kl37bu4cr3',
        'GrowthBook_experiments': 'experiment_web_cl_new_csi_v2.0%2Cexperiment_web_aa_test_202601.0%2Cexperiment_web_search_quantity_discount_promo.0%2Cexperiment_web_aa_2026_01_v1.0%2Cexperiment_web_swap_min_delivery_info_v1.6%2Cexperiment_web_delivery_after_promocode_v2.1%2C%20experiment_web_search_ds_bandit_4.1%2Cexperiment_main_page_pers_offer_web_2026_05_07.1',
        '_ym_visorc': 'b',
        'GrowthBook_Cookie_Experiments': 'exp_newui_chips.test%2C%20exp_web_chips_online.default%2C%20exp_big_card.Default%2C%20exp_product_page_by_blocks.default%2C%20exp_without_a_doorbell.test_A%2C%20exp_without_a_doorbell_new.default%2C%20exp_search_photo_positions.default%2C%20exp_new_navigation_web.test%2C%20exp_web_mobile_tabbar.test%2C%20exp_web_personal_promo_delivery_chips.test%2C%20exp_personal_promo_delivery_chips.default%2C%20exp_new_navigation_web_search.test%2C%20exp_new_navigation_web_actions.test%2C%20exp_leave_order_at_door.test%2C%20exp_leave_order_at_door_new.test%2C%20exp_unpin_tabbar.default%2C%20exp_br_1521_refresh_auth_token.default%2C%20exp_unpin_tabbar_v2.default%2C%20exp_start_page_mobweb.default%2C%20exp_new_counter_web.control%2C%20exp_ds_main_page_web_goods_waterfall.default',
        'tmr_detect': '0%7C1778934398738',
        'spid.d58d': '0d5a2eb8-df14-418e-ba33-e23583159a75.1777142065.2.1778934399.1777143324.2ade4935-c2da-4030-9abb-17c02ce167bf.df98c19c-b4f2-4bde-9f24-9db7d2650fd3.d7ed7aca-58fd-4e97-9225-56b5de1eb7d3.1778929010734.659',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://ya.ru/',
        'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        # 'cookie': 'User_Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F148.0.0.0%20Safari%2F537.36; Is_Search_Bot=false; agree_with_cookie=true; GrowthBook_user_id=fdf99ea2-b311-7e97-c3ff-75bb427460c7; App_Cache_MPK=mp300-b1de0bac2c257f3257bf5ef2eea4ecbc; App_Cache_CitySlug=moscow; PassportRefreshToken=; PassportAccessToken=; PassportExpiresIn=; UserSessionId=e578272b-f819-9908-9829-c390121c1c99; Utk_SessionToken=01FA44FD85685B724BBC5E4D93362E1E; iap.uid=f2e2bc5792b84e86805fac78a8c7ad40; App_Cache_City=%7B%22centerLat%22%3A%2255.75322%22%2C%22centerLng%22%3A%2237.622552%22%2C%22id%22%3A1%2C%22isDefault%22%3Atrue%2C%22mainDomain%22%3Afalse%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%9E%22%2C%22slug%22%3A%22moscow%22%7D; App_Cache_MissionAddressMode=%7B%22t%22%3A%22pickup%22%2C%22ids%22%3Atrue%2C%22ma%22%3A%7B%22i%22%3A3149%2C%22a%22%3A%220124%22%2C%22t%22%3A%22%D0%A2%D0%9A124%22%2C%22af%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%207-%D1%8F%20%D0%9A%D0%BE%D0%B6%D1%83%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%2C%209%20(%D0%A2%D0%A0%D0%A6%20%D0%9C%D0%BE%D0%B7%D0%B0%D0%B8%D0%BA%D0%B0)%22%2C%22ri%22%3A1%2C%22mt%22%3A%22HM%22%2C%22s%22%3Afalse%7D%7D; flocktory-uuid=c23b42bd-b510-4a3a-b22d-da4458c83842-5; tmr_lvid=35f569253036a15cf7e71521dbc75886; tmr_lvidTS=1777142063632; adrcid=AV4RKMBCoarA8ah9OIqjerg; _ym_uid=1777142064325930018; _ym_d=1777142064; agree_with_cookie=true; Utk_DvcGuid=964a9f25-271c-2aba-c33a-bd5100ac01db; Utk_MrkGrpTkn=3B3669E90394E50F2924CB14536D461F; User_Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F148.0.0.0%20Safari%2F537.36; Is_Search_Bot=false; _ym_isad=1; spses.d58d=*; domain_sid=4vtd8s78bmtXLwu3dinrB%3A1778929028631; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1779016279847%2C%22sl%22%3A%7B%22224%22%3A1778929879847%2C%221228%22%3A1778929879847%7D%7D; adrdel=1778929881370; qrator_jsid=1778928978.107.Lia7wHZqzD2xhuUl-44j4dv4ehempdjfidmu2a1kl37bu4cr3; GrowthBook_experiments=experiment_web_cl_new_csi_v2.0%2Cexperiment_web_aa_test_202601.0%2Cexperiment_web_search_quantity_discount_promo.0%2Cexperiment_web_aa_2026_01_v1.0%2Cexperiment_web_swap_min_delivery_info_v1.6%2Cexperiment_web_delivery_after_promocode_v2.1%2C%20experiment_web_search_ds_bandit_4.1%2Cexperiment_main_page_pers_offer_web_2026_05_07.1; _ym_visorc=b; GrowthBook_Cookie_Experiments=exp_newui_chips.test%2C%20exp_web_chips_online.default%2C%20exp_big_card.Default%2C%20exp_product_page_by_blocks.default%2C%20exp_without_a_doorbell.test_A%2C%20exp_without_a_doorbell_new.default%2C%20exp_search_photo_positions.default%2C%20exp_new_navigation_web.test%2C%20exp_web_mobile_tabbar.test%2C%20exp_web_personal_promo_delivery_chips.test%2C%20exp_personal_promo_delivery_chips.default%2C%20exp_new_navigation_web_search.test%2C%20exp_new_navigation_web_actions.test%2C%20exp_leave_order_at_door.test%2C%20exp_leave_order_at_door_new.test%2C%20exp_unpin_tabbar.default%2C%20exp_br_1521_refresh_auth_token.default%2C%20exp_unpin_tabbar_v2.default%2C%20exp_start_page_mobweb.default%2C%20exp_new_counter_web.control%2C%20exp_ds_main_page_web_goods_waterfall.default; tmr_detect=0%7C1778934398738; spid.d58d=0d5a2eb8-df14-418e-ba33-e23583159a75.1777142065.2.1778934399.1777143324.2ade4935-c2da-4030-9abb-17c02ce167bf.df98c19c-b4f2-4bde-9f24-9db7d2650fd3.d7ed7aca-58fd-4e97-9225-56b5de1eb7d3.1778929010734.659',
    }

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )
    #text = str(response.text).split('')[0] and str(response.text).split("")[1]
    return response.text

print(get_info_lenta("https://lenta.com/product/pechene-rossiya-228g-298147/"))

