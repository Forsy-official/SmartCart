
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
    cookies = {
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
        'qrator_jsid': '1779214312.589.xMO1f8iMUOWxMUN2-m6ps55j1l9flvtluqc8u923co6m3mm1f',
        'Utk_DvcGuid': 'edbc70f1-7a4f-c56c-7552-7e2d0a179356',
        'Utk_MrkGrpTkn': 'B6B1950FB790A4A99D472A6E3EF22B1B',
        'GrowthBook_Cookie_Experiments': 'exp_newui_chips.test%2C%20exp_web_chips_online.test%2C%20exp_big_card.test%2C%20exp_product_page_by_blocks.default%2C%20exp_without_a_doorbell.test_A%2C%20exp_without_a_doorbell_new.default%2C%20exp_search_photo_positions.default%2C%20exp_new_navigation_web.test%2C%20exp_web_mobile_tabbar.test%2C%20exp_web_personal_promo_delivery_chips.test%2C%20exp_personal_promo_delivery_chips.default%2C%20exp_new_navigation_web_search.test%2C%20exp_new_navigation_web_actions.test%2C%20exp_leave_order_at_door.test%2C%20exp_leave_order_at_door_new.test%2C%20exp_unpin_tabbar.default%2C%20exp_br_1521_refresh_auth_token.default%2C%20exp_unpin_tabbar_v2.default%2C%20exp_start_page_mobweb.default%2C%20exp_new_counter_web.control%2C%20exp_ds_main_page_web_goods_waterfall.default%2C%20exp_catalog_new_widgets_cms.default',
        'GrowthBook_experiments': 'experiment_web_cl_new_csi_v2.0%2Cexperiment_web_aa_test_202601.0%2Cexperiment_web_search_quantity_discount_promo.0%2Cexperiment_web_aa_2026_01_v1.0%2Cexperiment_web_delivery_after_promocode_v2.1%2C%20experiment_web_search_ds_bandit_4.1%2Cexperiment_main_page_pers_offer_web_2026_05_07.1',
        'User_Agent': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F148.0.0.0%20Safari%2F537.36',
        'Is_Search_Bot': 'false',
        'spses.d58d': '*',
        '_bge_ci': 'BA1.1.7794651279.1779214316',
        'acs_3': '%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1779300716185%2C%22sl%22%3A%7B%22224%22%3A1779214316185%2C%221228%22%3A1779214316185%7D%7D',
        'adrdel': '1779214316480',
        '_bge_uid2': '8141640746625702563',
        '_ym_isad': '2',
        'domain_sid': '4vtd8s78bmtXLwu3dinrB%3A1779214320674',
        '_ym_visorc': 'b',
        'tmr_detect': '0%7C1779217023022',
        'spid.d58d': '0d5a2eb8-df14-418e-ba33-e23583159a75.1777142065.5.1779217372.1778955041.07c3be66-904b-4b2a-b5b9-cccd3ddd0bc2.fab7e76f-050d-4137-b734-ce4374e2f240.36eaa6f4-5db0-4d12-ae4c-9c8beb5b70cb.1779214314892.387',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'client': 'angular_web_0.0.2',
        'content-type': 'application/json',
        'deviceid': 'edbc70f1-7a4f-c56c-7552-7e2d0a179356',
        'experiments': 'exp_recommendation_cms.true, exp_lentapay.test, exp_profile_bell.test, exp_cl_omni_authorization.test, exp_fullscreen.test, exp_onboarding_editing_order.test, exp_cart_new_carousel.default, exp_sbp_enabled.default, exp_profile_settings_email.default, exp_cl_omni_refusalprintreceipts.test, exp_search_suggestions_popular_sku.default, exp_cl_new_csi.control, exp_cl_new_csat.default, exp_delivery_price_info.test, exp_interval_jump.test, exp_cardOne_promo_type.test, exp_birthday_coupon_skus.test, exp_qr_cnc.test, exp_where_place_cnc.test, exp_editing_cnc_onboarding.test, exp_editing_cnc.test, exp_pickup_in_delivery.test, exp_welcome_onboarding.default, exp_where_place_new.default, exp_start_page.default, exp_default_payment_type.default, exp_start_page_onboarding.default, exp_search_new_logic.default, exp_referral_program_type.default, exp_new_action_pages.default, exp_items_by_rating.test, exp_can_accept_early.default, exp_online_subscription.default, exp_hide_cash_payment_for_cnc_wo_adult_items.default, exp_prices_per_quantum.test, exp_web_chips_online.test, exp_promo_without_benefit.default, exp_cart_forceFillDelivery.default, exp_banner_sbp_checkout_step_3.control, exp_badge_sbp_checkout_step_3.test_B, exp_kit_banner_sbp_checkout_step_3.default, exp_kit_badge_sbp_checkout_step_3.default, exp_profile_stories.test, exp_cl_new_ui_csi_comment.default, exp_in_app_update.default, exp_sorting_catalog.default, exp_aa_test_2025_04.control, exp_search_items_by_date.test_B, exp_product_page_by_blocks.default, exp_without_a_doorbell.test_A, exp_without_a_doorbell_new.default, exp_edit_payment_type.test, exp_edit_payment_type_new.default, exp_search_photo_positions.default, exp_new_matrix.test, exp_another_button_ch.default, exp_progressbar_and_title.test, exp_auto_fill_coupon.default, exp_promo_and_bonus.test, exp_about_cnc_optimization.default, exp_online_categories.default, exp_no_intervals.default, exp_web_b2b_excel_load.default, exp_cart_save_with_promo.default, exp_email_optional_full_registration.default, exp_new_navigation_web.test, exp_cl_new_rateapp.default, exp_similar_goods_cart.test, exp_cart_redesign_promocode.default, exp_search_new_filters.test, exp_loyalty_categories_labels.default, exp_search_multicard.test, exp_delivery_promocode_bd_coupon.default, exp_search_disable_fuzziness.default, exp_ui_catalog_level_2.default, exp_fullscreen_inapp_vs_native.test1, exp_search_collections_ranking.test, exp_search_elastic_tokens.default, exp_cl_new_tapbar.default, exp_cl_new_tapbar_tab.default, exp_search_my_choice_stock_priority.test_b, exp_cart_free_sample.default, exp_about_promocode.test_A, exp_personal_promo_detail_for_delivery.test_2, exp_search_combined_field.default, exp_search_unified.default, exp_web_personal_promo_detail_for_delivery.default, exp_web_personal_promo_delivery_chips.test, exp_b2b_web_mob_checkout.default, exp_personal_promo_delivery_chips.default, exp_ds_cnc_pers_recom.test, exp_ds_mntk_pers_recom.default, exp_shopping_statistics.default, exp_pin_create_button.default, exp_search_ui_catalog_pim.default, exp_search_video.default, exp_search_pinned_reviews.test, exp_sbp_instead_of_lenta_pay.default, exp_card1_start_page.default, exp_new_navigation_web_search.test, exp_new_navigation_web_actions.test, exp_status_assemble_completed.test, exp_cl_new_ui_csi_comment2.default, exp_online_subscription_discount.test, exp_start_page_button_notifications.default, exp_quick_checkout.default, exp_quick_checkout_update.default, exp_new_goods_widget_processing.default, exp_search_no_stock.true, exp_brief_description_promo.default, exp_new_offer_new_user_v1.default, exp_order_feedback_show.default, exp_leave_order_at_door.test, exp_leave_order_at_door_new.test, exp_search_quantity_discount_promo.control, exp_start_page_button_navigation_off.default, exp_obi_webview.true, exp_huawei_adjust_new_tokens.true, exp_import_goods_in_basket.default, exp_unpin_tabbar.default, exp_mna_orders_editing.default, exp_consent.default, exp_main_stories.test, exp_from_store_myself.default, exp_new_bs_catalog_startpage.default, exp_be_soon_show_explain_message.default, exp_startpage_mainpage_new_address_design.default, exp_bubble_discount_startpage_mainpage.test, exp_startpage_zone_description.default, exp_ds_pd_carousel.default, exp_ds_pers_recom_delivery_2.test, exp_search_ds_catboost_2.control, exp_novikov_test.OFF, exp_order_created_action_banner.default, exp_ds_mntk_pers_cat.default, exp_search_ds_empty_recom.default, exp_badges_pers_cashback.default, exp_temp_exp_ds_pd_carousel_android.default, exp_temp_exp_ds_pd_carousel_android_general.default, exp_temp_samesplit_check_f.default, exp_interval_jump_30.default, exp_temp_exp_ds_pd_carousel_ios_general.default, exp_search_purchased_badge.default, exp_pwa_cart.default, exp_pwa_checkout.default, exp_auto_detection_store_for_new_user.default, exp_return_available_items.default, exp_b2c_onboarding_send_cart.test, exp_b2b_send_cart.default, exp_b2c_send_cart.test, exp_cart_item_modify_version20.default, exp_auth_sber_id.default, exp_search_voice_search_ai.default, exp_startpage_redesign_qr_and_loy.default, exp_web_aa_2026_01_v1.control, exp_startpage_redesign_missions.default, exp_search_pdp_big_photo.default, exp_startpage_tab_shop_on_the_map.default, exp_startpage_logics_button_pickup.default, exp_open_screen_card1_profile_without_address.default, exp_web_cancel_to_edit_cnc.test, exp_ch_how_much_unit.test, exp_search_fd.default, exp_authorization_tg.default, exp_ds_cat_diversity.test, exp_more_about_price.default, exp_br_1521_refresh_auth_token.default, exp_kpp_aa.default, exp_unpin_tabbar_v2.default, exp_b2c_bot_web_send_cart.default, exp_nearest_hubs_new_logic.default, exp_new_bs_catalog_startpage_v2.default, exp_favorite_categories_description.default, exp_start_page_mobweb.default, exp_test_toggle_b2b_b2c_web.test, exp_startpage_free_delivery.default, exp_search_custom_qty.default, exp_allow_push_notifications.default, exp_time_track.default, exp_auth_call.default, exp_search_ds_bandit_3.default, exp_web_pickup_popup_map_2192.default, exp_new_counter_web.control, exp_ds_main_page_goods_waterfall.default, exp_startpage_hovering_basket_gr_2272.default, exp_yandex_pay_available.default, exp_pwa_vertical_pers_recom.default, exp_search_pdp_banner.default, exp_ds_main_page_web_goods_waterfall.default, exp_search_price_filter.default, exp_qr_code_action_banner.default, exp_gr_2584_auth_vk_id_yandex_id.default, exp_disable_delivery_price_info.default, exp_swap_empty_delivery_info.test_B, exp_swap_min_delivery_info.test_B, exp_authorization_vpn.test, exp_search_pdp_new_badges.default, exp_status_on_main.default, exp_status_on_landing.default, exp_time_in_minutes_gr_2527.default, exp_delivery_after_promocode.test, exp_offer_different_discounts.default, exp_b2b_profile_hide_sidebar.default, exp_edit_promocode.default, exp_web_cancel_to_promoedit.default, exp_main_page_new_mode_shop_v2.default, exp_cheap_no_intervals.default, exp_cart_photo_badge_packaging.default, exp_two_intervals.default, exp_cl_new_csat_comment.default, exp_cart_title_mode.default, exp_web_card_favoriteCategoriesWidget.default, exp_search_ds_bandit_4.test_a, exp_ch22405cartwithoutmonolith.test, exp_reason_for_cancellation.default, exp_search_new_plp.default, exp_pwa_profile.default, exp_fetch_deprecated_toggles_from_cdn.default, exp_main_page_new_button_shop_v2.default, exp_main_page_pers_offer_app.default, exp_main_page_pers_offer_web.test, exp_main_page_new_mode_content.default, exp_start_page_new_widgets_cms.default, exp_catalog_new_widgets_cms.default, exp_search_skip_catalog_level_2.default, exp_web_linking_sbp.efault, exp_price_for_tem_cart.default, exp_cart_switch_receiving_method.default, exp_collect_email_checkout.default, exp_ds_seasonal_cartpers_recom.default',
        'origin': 'https://lenta.com',
        'priority': 'u=1, i',
        'referer': 'https://lenta.com/',
        'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sessiontoken': '01FA44FD85685B724BBC5E4D93362E1E',
        'traceparent': '00-74cdc6dfb839729fe6b59487f767fd9b-6e339eea5a8dd13f-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        'x-delivery-mode': 'pickup',
        'x-device-brand': '',
        'x-device-id': 'edbc70f1-7a4f-c56c-7552-7e2d0a179356',
        'x-device-name': '',
        'x-device-os': 'Web',
        'x-device-os-version': '12.4.8',
        'x-device-web-platform': 'desktop_web',
        'x-domain': 'moscow',
        'x-organization-id': '',
        'x-platform': 'omniweb',
        'x-retail-brand': 'lo',
        'x-span-id': '6e339eea5a8dd13f',
        'x-trace-id': '74cdc6dfb839729fe6b59487f767fd9b',
        'x-user-session-id': 'e578272b-f819-9908-9829-c390121c1c99',
        # 'cookie': 'GrowthBook_user_id=fdf99ea2-b311-7e97-c3ff-75bb427460c7; App_Cache_MPK=mp300-b1de0bac2c257f3257bf5ef2eea4ecbc; App_Cache_CitySlug=moscow; PassportRefreshToken=; PassportAccessToken=; PassportExpiresIn=; UserSessionId=e578272b-f819-9908-9829-c390121c1c99; Utk_SessionToken=01FA44FD85685B724BBC5E4D93362E1E; iap.uid=f2e2bc5792b84e86805fac78a8c7ad40; App_Cache_City=%7B%22centerLat%22%3A%2255.75322%22%2C%22centerLng%22%3A%2237.622552%22%2C%22id%22%3A1%2C%22isDefault%22%3Atrue%2C%22mainDomain%22%3Afalse%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%9E%22%2C%22slug%22%3A%22moscow%22%7D; App_Cache_MissionAddressMode=%7B%22t%22%3A%22pickup%22%2C%22ids%22%3Atrue%2C%22ma%22%3A%7B%22i%22%3A3149%2C%22a%22%3A%220124%22%2C%22t%22%3A%22%D0%A2%D0%9A124%22%2C%22af%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%207-%D1%8F%20%D0%9A%D0%BE%D0%B6%D1%83%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%2C%209%20(%D0%A2%D0%A0%D0%A6%20%D0%9C%D0%BE%D0%B7%D0%B0%D0%B8%D0%BA%D0%B0)%22%2C%22ri%22%3A1%2C%22mt%22%3A%22HM%22%2C%22s%22%3Afalse%7D%7D; flocktory-uuid=c23b42bd-b510-4a3a-b22d-da4458c83842-5; tmr_lvid=35f569253036a15cf7e71521dbc75886; tmr_lvidTS=1777142063632; adrcid=AV4RKMBCoarA8ah9OIqjerg; _ym_uid=1777142064325930018; _ym_d=1777142064; agree_with_cookie=true; qrator_jsid=1779214312.589.xMO1f8iMUOWxMUN2-m6ps55j1l9flvtluqc8u923co6m3mm1f; Utk_DvcGuid=edbc70f1-7a4f-c56c-7552-7e2d0a179356; Utk_MrkGrpTkn=B6B1950FB790A4A99D472A6E3EF22B1B; GrowthBook_Cookie_Experiments=exp_newui_chips.test%2C%20exp_web_chips_online.test%2C%20exp_big_card.test%2C%20exp_product_page_by_blocks.default%2C%20exp_without_a_doorbell.test_A%2C%20exp_without_a_doorbell_new.default%2C%20exp_search_photo_positions.default%2C%20exp_new_navigation_web.test%2C%20exp_web_mobile_tabbar.test%2C%20exp_web_personal_promo_delivery_chips.test%2C%20exp_personal_promo_delivery_chips.default%2C%20exp_new_navigation_web_search.test%2C%20exp_new_navigation_web_actions.test%2C%20exp_leave_order_at_door.test%2C%20exp_leave_order_at_door_new.test%2C%20exp_unpin_tabbar.default%2C%20exp_br_1521_refresh_auth_token.default%2C%20exp_unpin_tabbar_v2.default%2C%20exp_start_page_mobweb.default%2C%20exp_new_counter_web.control%2C%20exp_ds_main_page_web_goods_waterfall.default%2C%20exp_catalog_new_widgets_cms.default; GrowthBook_experiments=experiment_web_cl_new_csi_v2.0%2Cexperiment_web_aa_test_202601.0%2Cexperiment_web_search_quantity_discount_promo.0%2Cexperiment_web_aa_2026_01_v1.0%2Cexperiment_web_delivery_after_promocode_v2.1%2C%20experiment_web_search_ds_bandit_4.1%2Cexperiment_main_page_pers_offer_web_2026_05_07.1; User_Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F148.0.0.0%20Safari%2F537.36; Is_Search_Bot=false; spses.d58d=*; _bge_ci=BA1.1.7794651279.1779214316; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1779300716185%2C%22sl%22%3A%7B%22224%22%3A1779214316185%2C%221228%22%3A1779214316185%7D%7D; adrdel=1779214316480; _bge_uid2=8141640746625702563; _ym_isad=2; domain_sid=4vtd8s78bmtXLwu3dinrB%3A1779214320674; _ym_visorc=b; tmr_detect=0%7C1779217023022; spid.d58d=0d5a2eb8-df14-418e-ba33-e23583159a75.1777142065.5.1779217372.1778955041.07c3be66-904b-4b2a-b5b9-cccd3ddd0bc2.fab7e76f-050d-4137-b734-ce4374e2f240.36eaa6f4-5db0-4d12-ae4c-9c8beb5b70cb.1779214314892.387',
    }

    json_data = {
        'selectionId': 310004284,
        'sort': {
            'type': 'popular',
            'order': 'desc',
        },
        'limit': 40,
        'offset': 0,
    }

    response = requests.post(
        url,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    t = response.text.split(',"name":')[-1]
    text = t.split(",")[0]
    ls = dict()
    ls["shop"] = "Лента"
    ls["product"] = text
    ls["price"] = None

    #
    return ls


def get_info_patyorka(url):
    cookies = {
        'spid': '1776538965928_c364545c03f5d240e70330cbb7b271ec_ktb16qobri0mdrd4',
        '_ym_uid': '1776538968737585761',
        '_ym_d': '1776538968',
        'spjs': '1779459815910_289c66f3_013526a2_58d87620bd7cda292ffd782950baf39c_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',
        'spsc': '1779459815910_2a0d584dfaab8c01919059c29ba63baf_0PP2fMHJOkse894VuAhD0HOuio3Y149XzGKZiMuRbkIZ',
        'SRV': 'a8e9ec24-0561-4675-9abb-61b3c8c6c894',
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
        # 'cookie': 'spid=1776538965928_c364545c03f5d240e70330cbb7b271ec_ktb16qobri0mdrd4; _ym_uid=1776538968737585761; _ym_d=1776538968; spjs=1779459815910_289c66f3_013526a2_58d87620bd7cda292ffd782950baf39c_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; spsc=1779459815910_2a0d584dfaab8c01919059c29ba63baf_0PP2fMHJOkse894VuAhD0HOuio3Y149XzGKZiMuRbkIZ; SRV=a8e9ec24-0561-4675-9abb-61b3c8c6c894',
    }

    params = {
        'mode': 'delivery',
        'include_restrict': 'true',
        'q': 'печенье',
        'limit': '12',
    }

    response = requests.get('https://5d.5ka.ru/api/catalog/v3/stores/35XY/search', params=params, cookies=cookies,
                            headers=headers)
    te = response.text.split(',"name":')[1]
    text = te.split(',')[0]
    pr = te.split('"prices":{"regular":')[1]
    price = pr.split(",")[0]
    ls = dict()
    ls["shop"] = "Пятёрочка"
    ls["product"] = text
    ls["price"] = price
    return ls
print(get_info_magnit("https://magnit.ru/product/1000026882-kubanskaya_burenka_moloko_past_2_5_0_93l_pl_but_vbd_6?shopCode=992301&shopType=6"))
print(get_info_lenta("https://lenta.com/product/keks-yagodnoe-lukoshko-s-vishnejj-rossiya-270g-18236/"))
print(get_info_patyorka("https://5ka.ru/product/khleb-sibirskiy-pekar-zernovoy-multizlakovyy-so-ln--4103219/"))
