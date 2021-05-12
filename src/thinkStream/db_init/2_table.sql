-- user data

USE thinkStream_user;

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) AUTO_INCREMENT NOT NULL,
  `mail` varchar(254) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` char(60) NOT NULL,
  `groups` varchar(50) NOT NULL,
  `created` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE IF NOT EXISTS `thoughts` (
  `id` int(11) AUTO_INCREMENT NOT NULL,
  `user_mail` varchar(254) NOT NULL,
  `thought` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX (`user_mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE IF NOT EXISTS `diaries` (
  `id` int(11) AUTO_INCREMENT NOT NULL,
  `user_mail` varchar(254) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `thought_id` int(11) NOT NULL,
  `body` TEXT NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`id`),
  INDEX (`user_mail`, `thought_id`),
  FOREIGN KEY fk_thoughts (`thought_id`) REFERENCES thoughts(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
