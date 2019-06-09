<?php

function curl_v1($url, $is_post = 1, $post_data = [])
    {

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        if ($is_post == 1) {
            curl_setopt($ch, CURLOPT_HTTPHEADER,
                [
                    'Content-Type: application/json',
                    'Content-Length: ' . strlen(json_encode($post_data))
                ]

            );
            // post数据
            curl_setopt($ch, CURLOPT_POST, 1);
            // post的变量
            curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
        }else{
            curl_setopt($ch, CURLOPT_HEADER, 0);
        }
        $data = curl_exec($ch);
        curl_close($ch);
        if (empty($data))
            return array();
        return $data;
        
    }
function curl_post($url, $is_post = 1, $post_data = [], $async = 1)
    {

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        if ($async == 1) {
            curl_setopt($ch, CURLOPT_TIMEOUT, 20);
        } else {
            curl_setopt($ch, CURLOPT_NOSIGNAL, 1);    //注意，毫秒超时一定要设置这个
            curl_setopt($ch, CURLOPT_TIMEOUT_MS, 100);  //超时毫秒
        }
        if ($is_post == 1) {
            curl_setopt($ch, CURLOPT_HTTPHEADER,
                [
                    'Content-Type: application/json',
                    'Content-Length: ' . strlen(json_encode($post_data))
                ]

            );
            // post数据
            curl_setopt($ch, CURLOPT_POST, 1);
            // post的变量
            curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
        }else{
            curl_setopt($ch, CURLOPT_HEADER, 0);
        }
        $data = curl_exec($ch);
        curl_close($ch);
        if (empty($data))
            return array();
        return json_decode($data, true);
        
    }
    $url = 'http://dev.api.agc.moviebook.cn/api/materialcategory/?format=json';
    $res = curl_post($url,0);
    var_dump($res);