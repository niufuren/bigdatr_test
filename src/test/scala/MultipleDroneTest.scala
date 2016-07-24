import org.scalatest.FlatSpec
import scala.collection.mutable.ListBuffer
import scala.io.Source

class MultipleDroneSpec extends FlatSpec {

  def fixture =
    new {
      val multipleDroneFirst = new MultipleDrone(2, 1)
      val multipleDroneSecond = new MultipleDrone(2, 2)
    }

  "A MultipleDrone class" should "be able to get the unique billboards that are photographed by two drones" in {
    val f = fixture
    f.multipleDroneFirst.snapshot.position = ListBuffer((0, 0), (0, 1))
    f.multipleDroneSecond.snapshot.position = ListBuffer((0, 0))
    assert(f.multipleDroneFirst.billboardUnionNum(f.multipleDroneSecond) === 2)

    f.multipleDroneSecond.snapshot.position = ListBuffer((1, 0))
    assert(f.multipleDroneFirst.billboardUnionNum(f.multipleDroneSecond) === 3)

  }

}
