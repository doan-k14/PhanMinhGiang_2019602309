from text_summarizing import TextSummarizing
import numpy as np

ts = TextSummarizing(5)
# paragraph = 'Tất cả bánh xu xê đều có hàn the. Bánh xu xê đang bị phường Nguyễn Trung Trực (Ba Đình, Hà Nội) cấm bán vì việc sản xuất bắt buộc phải dùng hàn the. Tuy nhiên, các cửa hàng trên phố Hàng Than vẫn làm bánh này khi có khách đặt mua làm lễ ăn hỏi. Trong buổi kiểm tra vệ sinh thực phẩm sáng 1/4, Sở Y tế Hà Nội đã phát hiện hàn the - chất bị cấm dùng trong thức ăm - trong mẻ bánh xu xê 100 cái của cửa hàng Hồng Ninh, 79 Hàng Than. Mảnh giấy quỳ ngả màu đỏ sẫm chứng tỏ hàm lượng hàn the rất cao. Theo bà chủ cửa hàng, vài tháng nay khi phường Nguyễn Trung Trực cấm bán bánh xu xê, bà không bày bán mặt hàng này nữa, trừ khi có khách đặt cho đám cưới đám hỏi. Tuy biết hàn the là chất bị cấm nhưng bà vẫn phải dùng vì chất phụ gia thay thế hàn the không làm được bánh xu xê. Ông Nguyễn Trọng Nghĩa, Phó chủ tịch UBND phường, giải thích: Chất phụ gia thay thế hàn the mà ngành y tế cho phép sử dụng tuy rất hiệu quả khi dùng sản xuất giò chả, bánh giò. nhưng nếu dùng sản xuất bánh xu xê thì không đạt yêu cầu. Bánh xu xê làm từ chất phụ gia này không đủ độ trong, độ dai và không bảo quản được lâu, chỉ để khoảng 2 ngày là chảy nước. Do muốn sản xuất bánh xu xê thì bắt buộc dùng hàn the nên để ngăn ngừa nguy cơ từ chất này đối với sức khỏe, từ vài tháng nay phường Nguyễn Trung Trực đã cấm sản xuất và bán bánh này. Hầu như không cửa hàng nào bày bán nữa nhưng nếu có khách đặt thì vẫn nhận. Theo ông Nghĩa, cấm bán bánh xu xê là một hạ sách, là điều cực chẳng đã vì đây là một mặt hàng truyền thống của phường và rất cần thiết cho lễ ăn hỏi theo phong tục Việt Nam. Tuy nhiên, hiện phường chưa có cách nào để vẫn duy trì mặt hàng này mà không ảnh hưởng đến sức khỏe người dân. Ông Lê Anh Tuấn, Giám đốc Sở Y tế, cho biết sẽ đề nghị các cơ quan nghiên cứu tìm ra một chất phụ gia mới an toàn mà vẫn đảm bảo các yêu cầu về độ ngon miệng, thời hạn bảo quản của bánh xu xê.'
paragraph = 'Công sở đậm dư âm Tết trong ngày đầu làm việc. Trong lịch công tác của các bộ ngành 3 ngày đầu năm hầu như không có những cuộc họp. Chương trình làm việc chính của các lãnh đạo là chúc Tết. Một số nơi còn ghi lịch làm việc: lãnh đạo giải quyết công việc thường xuyên tại cơ quan. 9h sáng, hội trường Bộ Giáo dục và Đào tạo rộn tiếng cười đùa, chúc tụng, tiếng ly rượu cụng nhau chan chát. Sau đó các vụ, phòng bắt đầu những cuộc gặp gỡ riêng. Buổi "làm việc" đầu năm kết thúc sớm, với bữa tiệc tân niên tại gia. "Ngày thường, cùng cơ quan đấy nhưng mấy khi có dịp đến nhà nhau. Năm qua, người thì xây nhà mới, người thì có con đầu lòng. Đầu xuân, mọi người trong phòng đến nhà nhau, vừa chúc Tết, thăm hỏi luôn", anh Tuấn, cán bộ Tổng công ty Dệt may Việt Nam tâm sự. Sau 2 màn tiệc ngọt tại cơ quan, 10h sáng, các thành viên trong phòng của Tuấn "đóng cửa" bắt đầu những cuộc viếng thăm truyền thống. "Hôm nay ai có việc gấp quá thì phải làm nhưng ít người như thế lắm. Cả sếp và nhân viên công ty tôi đều đi chúc Tết. Chúc Tết các phòng xong, chúng tôi đang triệu nhau đến thăm nhà mấy người đồng nghiệp, bạn bè gần đây", chị Nguyễn Thị Bích Thư, phòng Kỹ thuật, Công ty Thép Miền Nam, 56 Thủ Khoa Huân, quận 1 (TP HCM) hoan hỷ. Rộn ràng trong công sở, không khí xuân còn tràn ngập quanh các hàng quán cà phê. 9h sáng, nhưng các hàng quán trên đường Lý Tự Trọng, quận 1 (TP HCM) vẫn khá đông công chức. Họ kể chuyện chơi Tết, chúc tụng, trao lì xì cho nhau và vui vẻ cười đùa. Anh Hoàng, cán bộ một sở trên đường Lý Tự Trọng cho biết, ngày đầu năm, lãnh đạo sở gặp mặt lãnh đạo các phòng, ban, nhân viên, ăn kẹo, uống chút bia thân mật để động viên, lấy "khí thế" làm việc cho cả năm. Dư vị Tết có lẽ phải kéo dài thêm vài ngày nữa. Trao đổi với VnExpress, Chánh Văn phòng của một bộ cho rằng: "Đầu năm chơi nhiều hơn làm" đã thành lệ khó sửa. Lãnh đạo cơ quan biết nhưng cũng phải thông cảm. "Anh em mời nhau đến nhà chơi, đi làm muộn một chút mình cũng phải thông cảm, quy định cứng nhắc quá thì mất vui. Tuy nhiên, công việc cơ quan vẫn phải đảm bảo", ông này nói. Cũng có một thực tế là đầu năm, người dân cũng mải vui Tết, chưa đến các cơ quan công quyền. Do vậy, không tạo áp lực công việc đối với công chức. Phòng công chứng số 1 (Hà Nội) ngày thường đông nghịt khách nhưng sáng nay vắng hoe. Anh Nguyễn Chí Thiện, công chứng viên cho biết, cả sáng chỉ có khoảng 30 hồ sơ công chứng, thấp "kỷ lục" trong năm. Vắng khách, sẵn mứt Tết "tồn đọng", nhân viên quây quần ngồi uống nước, bàn chuyện du xuân. 11h trưa, nhiều công sở ở Hà Nội khá im ắng, các quán ăn thì đông nghẹt khách. "Sáng đi được một tour rồi, trưa tụ họp ở quán ăn lấy sức. Chiều đi vài nhà nữa rồi karaoke", Ngọc Linh, nhân viên kinh doanh một hãng ôtô lớn hào hứng. Với nhiều công chức, ngày đầu năm đi làm còn vui hơn Tết!'
# paragraph = 'Sân chơi cho trẻ em vẫn chỉ là khẩu hiệu. Mỗi khi hè về, "Tháng hành động vì trẻ em" tới, chuyện sân chơi cho thiếu nhi lại được nhiều người quan tâm hơn. Nhưng hè nào cũng vậy, trẻ vẫn cứ thiếu chỗ chơi. Những đô thị lớn như HN và TP HCM cũng không là ngoại lệ. Thường ngày, các điểm sinh hoạt văn hoá - thể thao dành cho thiếu nhi ở HN đã luôn quá tải. Đặc biệt là ở Cung Thiếu nhi, người ta đã phải tận dụng tối đa cơ sở vật chất, huy động thêm nhiều cộng tác viên, tăng ca học cả buổi tối. Công viên nước Hồ Tây cũng là một điểm thu hút đông trẻ em tới tham gia sinh hoạt, cho dù nơi đây giá vé không phải là "mềm" và không phải các trò chơi đều phù hợp với thiếu nhi. Trong khi đó, công viên Thủ Lệ (hay còn gọi là Vườn thú HN) có diện tích rộng, nhưng lại không "bắt mắt" trẻ, bởi chuồng thú thì hôi, hàng quán choán hết lối đi. Công viên Thống Nhất có địa thế đẹp, gần trung tâm thành phố, dễ tổ chức các khu vui chơi giải trí cho trẻ, nhưng lại rất ít các trò chơi mới. Những trò như: nhà gương, đu quay đã nhàm chán. Trong công viên, đây đó còn xuất hiện những chợ cóc bán tạp nham đủ thứ. Cảnh "tình tự" ở nhiều công viên diễn ra vô tư trước mắt trẻ. Các bậc phu huynh rất ngại cho con mình chơi đùa, sợ giẫm phải kim tiêm của dân chích hút. Trong khi các công viên chưa đáp ứng được nhu cầu chính đáng của mọi người dân, đặc biệt là trẻ em, thì hệ thống các nhà văn hoá thiếu nhi ở HN lại rất thiếu, nặng về hình thức. Phần lớn số 1.700 điểm vui chơi cấp phường, xã trên địa bàn HN chưa được xây dựng hoàn chỉnh, hoặc để đất trống. Thậm chí ở nhiều khu dân cư, các điểm vui chơi của trẻ em đã bị thu hẹp lại hoặc bị lấn chiếm, sử dụng sai mục đích. Tại khu chung cư Thanh Xuân Bắc, đơn vị thi công đã tự ý thay đổi công năng diện tích dành cho thiếu nhi. Rạp Kim Đồng - nơi một thuở chuyên chiếu phim cho thiếu nhi - nay bị chiếm làm quán bán bia. Một vài điểm vui chơi như Sega, Star Bowl, Cosmos luôn có nhiều thiếu nhi tới chơi, nhưng chủ yếu là con em gia đình khá giả, bởi giá vé ở đây khá cao. Tại TPHCM hiện cũng chưa một công trình nào được xây dựng đúng nghĩa là sân chơi dành cho thiếu nhi. Nhà văn hoá thiếu nhi thành phố có mặt bằng rộng, thu hút đông bạn nhỏ, đang trở thành quá tải, nhất là trong dịp hè và lễ hội. 24 nhà văn hoá thiếu nhi quận, huyện ngoài việc có dành chỗ cho thiếu nhi sinh hoạt, thì còn cho thuê mướn mặt bằng, hoặc "tranh thủ" mở đủ loại dịch vụ cho người lớn. Trong 4 "Ngày hội tuổi thơ" dịp 1.6, Nhà văn hoá thiếu nhi thành phố có trên 15.000 lượt người đến vui chơi. Trong khi đó, vào ngày thường, nơi đây chỉ đủ đón 1.000-1.500 trẻ. Trung bình mỗi tuần có trên 20.000 lượt trẻ tập trung ở khu vực này. Cũng hằng tuần, từ các tỉnh như Bình Dương, Đồng Nai, có hàng đoàn xe chở trẻ em đến Nhà văn hoá thiếu nhi của TP HCM để sinh hoạt, học các môn năng khiếu. Học sinh các huyện Hóc Môn, Củ Chi cũng đổ về đây cuối tuần. Do không đủ chỗ, các em vẫn phải ra ngồi học ở ghế đá. Lớp học chia làm nhiều suất. Phụ huynh phải trải chiếu ngồi đợi con em mình. Thỉnh thoảng, nhà văn hoá thiếu nhi thành phố lại đón trẻ ở các mái ấm, nhà mở về vui chơi, nên càng quá tải hơn. Khi dự án mở rộng đường Nam Kỳ Khởi Nghĩa thực thi, một phần diện tích không nhỏ của nơi này sẽ bị mất đi. Sân chơi vốn đã chật sẽ càng hẹp hơn. Ban lãnh đạo Nhà văn hoá thiếu nhi đang đề xuất UBND TP cho mở địa điểm ở vùng ven, hoặc xây dựng nhà văn hoá thiếu nhi mới quy mô hơn, nhưng đến nay vẫn chưa thực hiện được. Tại quận 1, Nhà văn hoá thiếu nhi khá khang trang, nhưng hội trường chính đã trở thành rạp kịch của sân khấu Idecaf. Ở đây chỉ có phòng để học, chứ không có trò chơi hay khoảng sân rộng cho trẻ em vui chơi (khoảng sân này đã được trưng dụng thành bãi để xe và quán cà phê). Khu đô thị mới Phú Mỹ Hưng, dù được thiết kế phục vụ an sinh của cộng đồng, nhưng khu vui chơi của trẻ con vẫn thường bị "bỏ quên" trong dự án. Theo kiến trúc sư Võ Thành Lân, ở TPHCM chưa có công trình nào dành cho trẻ em đạt chuẩn. Nhiều dự án nhấn mạnh yếu tố làm sân chơi cho thiếu nhi, nhưng làm hay không là chuyện khác.'

ts.para2vec_list(paragraph)
clusters = ts.clustering()
close_index_vec_list = ts.find_center_vec(clusters)
vec_for_summary = [ts.vec_list[index] for index in close_index_vec_list]
summary = ts.we.veclist2para(vec_for_summary)
print(summary)