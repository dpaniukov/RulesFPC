args=commandArgs(trailingOnly=TRUE)
print(args)
FD=read.table(args[1],F)
motpars=read.table(args[2],F)

if(file.exists(args[3])){

}


pdf("QA_figs.pdf")
par(mfrow=c(3,1))
plot(1:length(FD$V1),FD$V1,xlab="Volume",ylab="Framewise Displacement",type='lines',main=paste("Scrubbed Volumes = ",sum(FD$V1>0.9),sep=""))
abline(h=0.9,col='red',lwd=2)



plot(1:length(motpars$V1),motpars$V1,lwd=2,xlab="Volume",ylab="Rotations (rad)",type="lines",ylim=c(min(motpars[,1:3]),max(motpars[,1:3])))
lines(1:length(motpars$V1),motpars$V2,lwd=2,col='red')
lines(1:length(motpars$V1),motpars$V3,lwd=2,col='blue')
legend("topright",c("X","Y","Z"),col=c('black','red','blue'),lwd=c(2,2,2))


plot(1:length(motpars$V1),motpars$V4,lwd=2,xlab="Volume",ylab="Translations (mm)",type='lines',ylim=c(min(motpars[,4:6]),max(motpars[,4:6])))
lines(1:length(motpars$V1),motpars$V5,lwd=2,col='red')
lines(1:length(motpars$V1),motpars$V6,lwd=2,col='blue')
legend("topright",c("X","Y","Z"),col=c('black','red','blue'),lwd=c(2,2,2))

dev.off()


TDS_motpars=rbind(t(c(0,0,0,0,0,0)),motpars[1:(length(motpars$V1)-1),]-motpars[2:length(motpars$V1),])

if(file.exists(args[3])){
	
scrubdes=read.table(args[3],F)

write.table(data.frame(motpars,TDS_motpars,scrubdes),'confound.txt',row.names=F,col.names=F)
write.table(data.frame(scrubdes),'conf_scrub.txt',row.names=F,col.names=F)
}else{write.table(data.frame(motpars,TDS_motpars),'confound.txt',row.names=F,col.names=F)
	file.create('conf_scrub.txt')
	}






