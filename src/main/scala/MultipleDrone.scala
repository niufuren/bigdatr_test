import scala.io.Source

class MultipleDrone(val totalDrone: Int, val order: Int) extends Drone {

  val totalDroneNum: Int = totalDrone
  val orderIndex: Int = order

  def readProcessCommands(fileName: String) {
    val source = Source.fromFile(fileName)
    var instructorCount = 1
    for (instructor <- source) {

      if (instructorCount <= totalDroneNum) {
        if (instructorCount == orderIndex) process(instructor)

      } else {
        if (orderIndex != totalDroneNum) {
          if (instructorCount % totalDroneNum == orderIndex) process(instructor)

        } else {
          if (instructorCount % totalDroneNum == 0) process(instructor)

        }

      }

      instructorCount = instructorCount + 1

    }

    source.close
  }

  def billboardUnionNum(drone: Drone): Int = {
    val billboardSelf = snapshot.position
    val billboardAnother = drone.snapshot.position

    val allBillboard = (billboardSelf ++ billboardAnother).toSet

    val billboardNum = allBillboard.size

    return billboardNum
  }

}

object MultipleDrone extends App {

  val fileName = args(0)
  val droneFirst = new MultipleDrone(2, 1)
  droneFirst.readProcessCommands(fileName)
  val droneFirstPosition = droneFirst.getCoordinate

  val droneSecond = new MultipleDrone(2, 2)
  droneSecond.readProcessCommands(fileName)
  val droneSecondPosition = droneSecond.getCoordinate

  val billboardNum = droneFirst.billboardUnionNum(droneSecond)

  println("The number of billboards that are captured" +
    " by two drones at least once is " + billboardNum)
  println("The coordinate of the final location of the first drone is " +
          droneFirstPosition)
  println("The coordinate of the final location of the second drone is " +
          droneSecondPosition)

}
