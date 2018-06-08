/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : seo

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-06-08 10:52:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `www_xiaoshiseo_com`
-- ----------------------------
DROP TABLE IF EXISTS `www_xiaoshiseo_com`;
CREATE TABLE `www_xiaoshiseo_com` (
  `id` int(255) NOT NULL AUTO_INCREMENT COMMENT '唯一ID递增',
  `url` varchar(255) NOT NULL COMMENT '网站网址',
  `baidu_rank` int(20) NOT NULL COMMENT '百度权重',
  `word_num` varchar(255) NOT NULL COMMENT '关键词数量',
  `about_ip` varchar(255) NOT NULL COMMENT '预估IP',
  `baidu_site` varchar(255) NOT NULL COMMENT '百度收录',
  `baidu_site1` varchar(255) NOT NULL COMMENT '百度最近1天收录',
  `baidu_site7` varchar(255) NOT NULL COMMENT '百度最近7天收录',
  `baidu_site30` varchar(255) NOT NULL COMMENT '百度最近30天收录',
  `site_360` varchar(255) NOT NULL COMMENT '360收录',
  `site_sogo` varchar(255) NOT NULL COMMENT '搜狗收录',
  `date` varchar(255) NOT NULL COMMENT '日期',
  PRIMARY KEY (`id`),
  UNIQUE KEY `date` (`date`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of www_xiaoshiseo_com
-- ----------------------------
INSERT INTO `www_xiaoshiseo_com` VALUES ('1', 'www.xiaoshiseo.com', '0', '39', '0', '297', '0', '0', '0', '14', '', '2018-06-08');
