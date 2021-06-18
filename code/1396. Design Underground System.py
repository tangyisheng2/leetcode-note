class UndergroundSystem:

    def __init__(self):
        self.customer_travel_record = {}  # 存储「正在旅行的旅客」当前的旅行信息：{id: start_station, time}
        self.station_time = {}  # 存储从a到b的站点旅行人数和总时间{(a, b): (time_sum, person_cnt)}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        """
        进站：在进站时需要先检查乘客是否已经进站（一个乘客只能进站一次）
        :param id: 乘客的ID
        :param stationName: 始发站名字
        :param t: 进站时间
        :return: None
        """
        if id not in self.customer_travel_record:  # 如果乘客没有进站记录（正常情况）
            self.customer_travel_record.update({id: (stationName, t)})  # 在旅行中的乘客中添加该记录
        else:  # 如果已经进站了（异常情况）
            return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """
        出站：需要有进站进站记录的旅客才可以进行出站
        :param id: 乘客的ID
        :param stationName: 终点站名字
        :param t: 出站时间
        :return: None
        """
        if id in self.customer_travel_record:  # 如果已进站的记录中有旅客的信息
            start_station, start_time = self.customer_travel_record.pop(id)  # 先获取旅客的进站信息，并在正在旅行的游客中删除该游客（已经出站就不算正在旅行了）
            if (start_station, stationName) not in self.station_time:  # 检查旅行人数和总时间记录中有无该名旅客旅行的路线（用于统计）
                self.station_time.update({(start_station, stationName): [0, 0]})  # 新增记录
            self.station_time[(start_station, stationName)][0] += t - start_time  # 在已有记录中加上该旅客的用时
            self.station_time[(start_station, stationName)][1] += 1  # 已有记录中人数+1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        """
        获取平均时间
        :param startStation: 始发站
        :param endStation: 终点站
        :return:
        """
        if (startStation, endStation) in self.station_time:
            time = self.station_time[(startStation, endStation)][0]  # 获取路线总共耗时
            people_cnt = self.station_time[(startStation, endStation)][1]  # 获取打成路线的人数
            return time / people_cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20)  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22)  # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise",
                                 "Cambridge")  # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton",
                                 "Waterloo")  # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24)
undergroundSystem.getAverageTime("Leyton", "Waterloo")  # return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38)  # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton",
                                 "Waterloo")  # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
