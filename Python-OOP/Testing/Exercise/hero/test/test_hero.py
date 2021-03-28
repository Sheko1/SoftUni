from Testing.Exercise.hero.project.hero import Hero
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("TestUser", 10, 50, 25)
        self.enemy = Hero("TestEnemy", 15, 40, 35)

    def test_hero_battle__when_you_try_to_fight_yourself__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_hero_battle__when_health_is_0__expect_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle__when_health_is_below_0__expect_value_error(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle__when_enemy_health_is_0__expect_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(context.exception))

    def test_hero_battle__when_enemy_health_is_below_0__expect_value_error(self):
        self.enemy.health = -1

        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(context.exception))

    def test_hero_battle__when_hero_and_enemy_health_are_0_after_fight__expect_draw(self):
        self.hero.damage = 5
        self.enemy.level = 10
        self.enemy.damage = 5
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_hero_battle__when_hero_and_enemy_health_are_below_0_after_fight__expect_draw(self):
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_hero_battle__when_enemy_health_is_0_after_fight__expect_win(self):
        self.enemy.level = 1
        self.enemy.damage = 1
        self.hero.damage = 4

        self.assertEqual("You win", self.hero.battle(self.enemy))
        self.assertEqual(11, self.hero.level)
        self.assertEqual(54, self.hero.health)
        self.assertEqual(9, self.hero.damage)

    def test_hero_battle__when_enemy_health_is_below_0_after_fight__expect_win(self):
        self.enemy.level = 1
        self.enemy.damage = 1

        self.assertEqual("You win", self.hero.battle(self.enemy))
        self.assertEqual(11, self.hero.level)
        self.assertEqual(54, self.hero.health)
        self.assertEqual(30, self.hero.damage)

    def test_hero_battle__when_hero_health_is_0_after_fight__expect_lose(self):
        self.enemy.level = 5
        self.enemy.damage = 10
        self.hero.damage = 1
        self.hero.level = 1

        self.assertEqual("You lose", self.hero.battle(self.enemy))
        self.assertEqual(6, self.enemy.level)
        self.assertEqual(44, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test_hero_battle__when_hero_health_is_below_0_after_fight__expect_lose(self):
        self.hero.damage = 1
        self.hero.level = 1

        self.assertEqual("You lose", self.hero.battle(self.enemy))
        self.assertEqual(16, self.enemy.level)
        self.assertEqual(44, self.enemy.health)
        self.assertEqual(40, self.enemy.damage)

    def test_hero_str_method(self):
        expect = f"Hero TestUser: 10 lvl\n" \
               f"Health: 50\n" \
               f"Damage: 25\n"

        self.assertEqual(expect, str(self.hero))
